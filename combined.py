import streamlit as st
import pandas as pd
import base64
import joblib
import numpy as np
import json
from thefuzz import fuzz, process
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import io
import html
from code import fetch_jobs
import google.generativeai as genai
from streamlit_js_eval import streamlit_js_eval
import random
import re

# --- Page and State Setup ---
st.set_page_config(
    page_title="SkillSpread : Level Up. Break In. Stand Out",
    page_icon="🎓",
    layout="wide"
)

# Initialize session state variables to give the app memory
if "analysis_done" not in st.session_state:
    st.session_state["analysis_done"] = False
if "generated_points" not in st.session_state:
    st.session_state["generated_points"] = None
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Ask me for a learning roadmap or project ideas!"}]


# --- Helper, GenAI, and Skill Processing Functions ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f: data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError: return None

def create_prompt(skills, job_description):
    return f"""As an expert career coach, based on these skills: {skills} and this job description: {job_description}, write 3-5 powerful resume bullet points starting with action verbs. Focus on matching the user's skills to the job requirements without inventing skills."""

def generate_response(prompt):
    try:
        genai.configure(api_key=st.secrets["gemini"]["api_key"])
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"An error occurred with the AI model: {e}")
        return None

skill_normalizer = {"powerbi": "power bi", "ml": "machine learning", "sql": "sql", "py": "python"}
def normalize_skill(skill):
    return skill_normalizer.get(skill.lower().strip(), skill.lower().strip())

def fuzzy_match(skill, skill_list, threshold=65):
    if not skill or not skill_list: return None
    match, score = process.extractOne(skill, skill_list, scorer=fuzz.token_set_ratio)
    return match if score >= threshold else None

def clean_text(text):
    # Lowercase + remove punctuation
    return re.sub(r"[^\w\s]", " ", text.lower())

def display_jobs(jobs, user_skills):
    if not user_skills:
        st.info("⚠️ No skills provided to match against job descriptions.")
        return

    for job in jobs:
        raw_text = (job.get("title", "") + " " + job.get("description", ""))
        text_to_search = improve_clean_text(raw_text)

        matched_skills_in_job = []

        for original_skill in user_skills:
            skill_found = False
            normalized_skill = enhanced_normalize_skill(original_skill)

            # Method 1: Direct substring search
            if normalized_skill in text_to_search:
                matched_skills_in_job.append(original_skill)
                skill_found = True
                continue

            # Method 2: Multi-word skills
            skill_words = normalized_skill.split()
            if len(skill_words) > 1:
                if all(word in text_to_search for word in skill_words):
                    matched_skills_in_job.append(original_skill)
                    skill_found = True
                    continue

            # Method 3: Token matching
            tokens = set(text_to_search.split())
            if normalized_skill in tokens:
                matched_skills_in_job.append(original_skill)
                skill_found = True
                continue

            # Method 4: Fuzzy matching (lower threshold since descriptions are short)
            if fuzz.partial_ratio(normalized_skill, text_to_search) >= 70:
                matched_skills_in_job.append(original_skill)
                skill_found = True
                continue

            # Method 5: Skill variations
            skill_variations = get_skill_variations(normalized_skill)
            for variation in skill_variations:
                if variation in text_to_search:
                    matched_skills_in_job.append(original_skill)
                    skill_found = True
                    break

        matched_skills_in_job = list(dict.fromkeys(matched_skills_in_job))

        if not matched_skills_in_job:
            skills_str = "Check full job posting for additional requirements"
            skill_color = "#6c757d"
        else:
            skills_str = ", ".join(matched_skills_in_job)
            skill_color = "#006400"

        # Clean job card
        st.markdown(
            f"""
            <div style="border:1px solid #99c2ff; border-radius:10px; padding:15px; margin-bottom:15px; 
                        background-color:#d6eaff;">
                <h4 style="margin:0; color:#003366;">{job.get("title", "No Title")}</h4>
                <p style="margin:3px 0; color:#004080;">
                    <b>{job.get("company", {}).get("display_name", "Unknown Company")}</b> | 📍 {job.get("location", {}).get("display_name", "Unknown Location")}
                </p>
                <p style="margin:5px 0; color:#333;">{job.get("description", "No description available")[:220]}...</p>
                <p style="margin:5px 0; color:{skill_color};"><b>Matching skills:</b> {skills_str}</p>
                <a href="{job.get("redirect_url", "#")}" target="_blank" 
                   style="display:inline-block; margin-top:10px; background-color:#007bff; color:white; 
                          padding:8px 16px; text-decoration:none; border-radius:6px; font-weight:bold;">
                    🔗 View Full Job Posting
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("")


# Also, update your get_skill_variations to include more HTML/CSS variations:
def get_skill_variations(skill):
    """Return common variations and abbreviations for skills"""
    variations = {
        'html': ['html5', 'hypertext markup language', 'markup'],
        'css': ['css3', 'cascading style sheets', 'styling'],
        'python': ['py', 'python3'],
        'javascript': ['js', 'node.js', 'nodejs', 'ecmascript'],
        'machine learning': ['ml', 'ai', 'artificial intelligence'],
        'sql': ['mysql', 'postgresql', 'sqlite', 'database'],
        'power bi': ['powerbi', 'power-bi'],
        'artificial intelligence': ['ai', 'machine learning', 'ml'],
        'user experience': ['ux', 'ui/ux', 'user interface'],
        'user interface': ['ui', 'ui/ux'],
        'react': ['reactjs', 'react.js'],
        'angular': ['angularjs'],
        'node.js': ['nodejs', 'node js'],
        'amazon web services': ['aws'],
        'google cloud platform': ['gcp'],
        'microsoft azure': ['azure']
    }

    return variations.get(skill.lower(), [skill])



def improve_clean_text(text):
    """Enhanced text cleaning function"""
    if not text:
        return ""

    # Convert to lowercase
    text = text.lower()

    # Replace common separators with spaces
    text = re.sub(r"[/\-_+]", " ", text)

    # Remove punctuation but keep spaces
    text = re.sub(r"[^\w\s]", " ", text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


# Enhanced skill normalizer
enhanced_skill_normalizer = {
    "powerbi": "power bi",
    "power-bi": "power bi",
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "sql": "sql",
    "py": "python",
    "js": "javascript",
    "nodejs": "node.js",
    "reactjs": "react",
    "angularjs": "angular",
    "css3": "css",
    "html5": "html",
    "aws": "amazon web services",
    "gcp": "google cloud platform"
}


def enhanced_normalize_skill(skill):
    """Enhanced skill normalization"""
    clean_skill = skill.lower().strip()
    return enhanced_skill_normalizer.get(clean_skill, clean_skill)


# --- Initialize chat state ---
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "assistant", "content": "Hi! I am your AI Career Mentor 🤖. Ask me about learning roadmaps, skill gaps, or project ideas!"}
    ]

if st.session_state.get("rerun_flag", False):
    st.session_state["rerun_flag"] = False
    st.experimental_rerun()  # or just st.stop() if rerun logic is handled


# --- UI Setup ---
img_base64 = get_base64_of_bin_file("logo.png")
if img_base64:
    st.markdown(f"<div style='text-align: center; margin-top: -90px;'><img src='data:image/png;base64,{img_base64}' width='250' style='margin-bottom: -50px';/></div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>🚀 SkillSpread : Level Up. Break In. Stand Out</h1>", unsafe_allow_html=True)
st.write("👋 Welcome to SkillSpread - your personal guide to landing a dream job by identifying required skills.")
st.markdown("---")

# --- Data & Model Loading ---
@st.cache_data
def load_data():
    data = pd.read_csv("skillspread_dataset.csv")
    job_roles_dataset = pd.read_csv("realistic_unique_job_roles_dataset.csv")
    all_skills = set(job_roles_dataset["Skills"])
    roles_from_data = sorted(data['job_role'].str.title().unique())
    return data, all_skills, roles_from_data
@st.cache_resource
def load_models():
    model = joblib.load("job_role_predictor.pkl")
    vectorizer = joblib.load("skill_vectorizer.pkl")
    return model, vectorizer, model.classes_
data, all_skills, roles_from_data = load_data()
model, vectorizer, job_roles = load_models()

# --- User Inputs Form ---
if not st.session_state.get("analysis_done", False):
    with st.form("input_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Enter Your name", placeholder="Type Here...")
            skills = st.text_area('Enter your skills', placeholder='separate your skills with a comma')
        with col2:
            job_role = st.selectbox("Enter a job role", options=['Select'] + roles_from_data)
        analyze_button = st.form_submit_button('Analyze Skills', use_container_width=True)
        if analyze_button:
            if job_role == "Select" or not skills.strip():
                st.error("Please select a job role and enter at least one skill.")
            else:
                st.session_state.analysis_done = True
                st.session_state.name = name
                st.session_state.job_role = job_role

                # Store ORIGINAL skills for display purposes
                st.session_state.original_skills = [s.strip() for s in skills.split(",")]

                # Store NORMALIZED skills for matching logic
                user_skills_cleaned = [enhanced_normalize_skill(s.strip()) for s in skills.split(",")]
                st.session_state.user_skills_cleaned = user_skills_cleaned

                index = data[data["job_role"] == job_role.lower()].index[0]
                st.session_state.index = index
                core_skills = [enhanced_normalize_skill(s.strip()) for s in data.iat[index, 1].split(",")]
                st.session_state.core_skills = core_skills
                optional_skills = [enhanced_normalize_skill(s.strip()) for s in data.iat[index, 2].split(",")]
                st.session_state.optional_skills = optional_skills
                st.session_state.matching_core_skills = list(
                    set(m for s in user_skills_cleaned if (m := fuzzy_match(s, core_skills))))
                st.session_state.missing_core_skills = [s for s in core_skills if
                                                        s not in st.session_state.matching_core_skills]
                st.session_state.matching_optional_skills = list(
                    set(m for s in user_skills_cleaned if (m := fuzzy_match(s, optional_skills))))
                st.session_state.missing_optional_skills = [s for s in optional_skills if
                                                            s not in st.session_state.matching_optional_skills]
                st.session_state.all_matched_skills = list(
                    set(st.session_state.matching_core_skills + st.session_state.matching_optional_skills))
                st.session_state.valid_user_skills = [s for s in user_skills_cleaned if
                                                      fuzzy_match(s, all_skills, threshold=85)]
                st.session_state.generated_points = None
                st.rerun()

# --- Main Display Logic ---
if st.session_state.get("analysis_done",False):
    if st.button("⬅️ Start New Analysis"):
        st.session_state.analysis_done = False; st.session_state.messages = None; st.session_state.generated_points = None
        st.rerun()

    st.markdown(f"### Hi **{st.session_state.name or 'user'}** 👋 here's your personalized report for **{st.session_state.job_role}**!")
    st.subheader("🧠 Core Skills Analysis")
    if st.session_state.matching_core_skills:
        st.success(f"🎉 Skills you already have: {', '.join(st.session_state.matching_core_skills)}")
    else:
        st.warning("Looks like you're starting from scratch🔥 — but that's okay! Let’s build your skill set step by step.")
    if st.session_state.missing_core_skills:
        st.error(f"⚠️ Core skills you need to learn: {', '.join(st.session_state.missing_core_skills)}")
        st.subheader("📚 Learn Your Missing Core Skills")
        resources_raw = data.iat[st.session_state.index, 3]
        try:
            decoded_once = json.loads(resources_raw)
            resources_dict = json.loads(decoded_once) if isinstance(decoded_once, str) else decoded_once
        except Exception:
            resources_dict = {}
        core_table_data = [{"Skill": s.title(), "Free": resources_dict.get(s, {}).get("free", "N/A"), "Paid": resources_dict.get(s, {}).get("paid", "N/A")} for s in st.session_state.missing_core_skills]
        if core_table_data:
            st.table(core_table_data)
    else:
        st.success("🎯 You're already equipped with all the core skills for this role. Great job!")
    st.divider()
    st.subheader("✨ Optional Skills Analysis")
    if st.session_state.matching_optional_skills:
        st.success(f"💡 Optional skills you have: {', '.join(st.session_state.matching_optional_skills)}")
    if st.session_state.missing_optional_skills:
        st.info(f"📌 Optional skills to explore: {', '.join(st.session_state.missing_optional_skills)}")
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🔮 Predicted Role Based on Your Skills")
        if st.session_state.valid_user_skills:
            st.success("🎯 Top 3 Predicted Roles:")
            valid_skills_text = ", ".join(list(set(st.session_state.valid_user_skills)))
            X_input = vectorizer.transform([valid_skills_text])
            probas = model.predict_proba(X_input)[0]
            top3_idx = np.argsort(probas)[::-1][:3]
            for rank, idx in enumerate(top3_idx, start=1):
                role = job_roles[idx]
                st.write(f"**{rank}. {role}**")
        else:
            st.warning("⚠️ Enter valid skills for a role prediction.")
    with col2:
        st.subheader("🚀 Skills Completion Percentage")
        actual_core = len(st.session_state.core_skills) if st.session_state.core_skills else 1
        actual_optional = len(st.session_state.optional_skills) if st.session_state.optional_skills else 1
        core_weight = (len(st.session_state.matching_core_skills) / actual_core) * 80
        optional_weight = (len(st.session_state.matching_optional_skills) / actual_optional) * 20
        per = core_weight + optional_weight; per = min(per, 100)
        cmap = mcolors.LinearSegmentedColormap.from_list("custom_gradient", ["#d9534f", "#f0ad4e", "#5cb85c"])
        norm = mcolors.Normalize(vmin=0, vmax=100); main_color = cmap(norm(per))
        fig, ax = plt.subplots(figsize=(2, 2))
        ax.pie([per, 100 - per], colors=[main_color, "#333333"], startangle=90, wedgeprops=dict(width=0.3))
        ax.text(0, 0, f"{per:.0f}%", ha='center', va='center', fontsize=12, fontweight='bold', color=main_color)
        ax.axis('equal'); buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=150, bbox_inches='tight', transparent=True)
        st.image(buf, width=150)
    st.markdown("---")
    # --- Tabbed Interface for Tools ---
    job_tab, resume_tab = st.tabs(["🔍 Find Relevant Jobs", "📝 AI Resume Builder"])
    with job_tab:
        st.subheader("Find Jobs Based on Your Profile")
        inner_tab1, inner_tab2 = st.tabs(["🔮 By Predicted Role", "🛠️ By Your Skills"])

        # 🔮 By Predicted Role
        with inner_tab1:
            if st.session_state.valid_user_skills:
                top_role = job_roles[
                    np.argmax(
                        model.predict_proba(
                            vectorizer.transform(
                                [", ".join(list(set(st.session_state.valid_user_skills)))]
                            )
                        )[0]
                    )
                ]
                st.info(f"Showing jobs for your top predicted role: **{top_role}**")
                with st.spinner(f"Fetching jobs for {top_role}..."):
                    # Keep role-based search as requested
                    jobs = fetch_jobs(top_role)
                    jobs = sorted(
                        jobs,
                        key=lambda job: sum(
                            skill.lower() in job.get("description", "").lower()
                            for skill in st.session_state.user_skills_cleaned
                        ),
                        reverse=True,
                    )

                    original_skills = st.session_state.get("original_skills", st.session_state.user_skills_cleaned)
                    display_jobs(jobs[:5], original_skills)
            else:
                st.caption("Enter at least one valid skill to see jobs based on your predicted role.")

        # 🛠️ By Your Skills
        with inner_tab2:
            if st.session_state.user_skills_cleaned:
                query_skills = ", ".join(st.session_state.user_skills_cleaned)
                st.info(f"Showing jobs for skills: **{query_skills}**")
                with st.spinner(f"Fetching jobs for your skills..."):
                    jobs = fetch_jobs(query_skills)
                    jobs = sorted(
                        jobs,
                        key=lambda job: sum(
                            skill.lower() in job.get("description", "").lower()
                            for skill in st.session_state.user_skills_cleaned
                        ),
                        reverse=True,
                    )

                    # ✅ Use the ORIGINAL skills (not normalized) for display
                    original_skills = [s.strip() for s in st.session_state.get("original_skills", [])]
                    display_jobs(jobs[:5], original_skills if original_skills else st.session_state.user_skills_cleaned)
            else:
                st.caption("Enter skills to see relevant jobs.")

    with resume_tab:
        st.subheader("AI Resume Bullet Point Generator")
        job_desc = st.text_area("Paste a Job Description Here to get started", height=200)
        if st.button("Generate Resume Points"):
            if not job_desc.strip():
                st.warning("Please paste a job description.")
            else:
                with st.spinner("✨ Your AI career coach is writing..."):
                    user_skills_str = ", ".join(st.session_state.all_matched_skills)
                    prompt = create_prompt(user_skills_str, job_desc)
                    generated_points = generate_response(prompt)
                    st.session_state.generated_points = generated_points
        if st.session_state.generated_points:
            st.subheader("✅ Your AI-Generated Resume Points")
            st.markdown(st.session_state.generated_points)



if st.session_state.get("analysis_done", False):
    st.markdown("### 🤖 AI Career Chatbot")

    with st.form(key="chat_form", clear_on_submit=True):
        user_message = st.text_input("Type your question here...")
        send_btn = st.form_submit_button("Send")

    def generate_chatbot_reply(user_message):
        # Gather context
        user_skills = ", ".join(st.session_state.get("user_skills_cleaned", []))
        matching_core = ", ".join(st.session_state.get("matching_core_skills", []))
        missing_core = ", ".join(st.session_state.get("missing_core_skills", []))
        job_role = st.session_state.get("job_role", "Not specified")

        # Build context-aware prompt
        context = f"""
        You are an AI Career Mentor. The user is targeting the role: {job_role}.
        Their known skills: {user_skills}.
        Skills they already match: {matching_core}.
        Skills they are missing: {missing_core}.
        Based on this, answer their question in a personalized way.
        User's question: {user_message}
        """
        return generate_response(context)

    # Friendly placeholder options
    thinking_texts = [
        "✨ Thinking about the best path for you...",
        "📚 Looking at your skills and job role...",
        "🚀 Planning your career roadmap...",
        "🤖 Crunching data to give you advice..."
    ]

    # Handle new user input
    if send_btn and user_message:
        st.session_state.chat_messages.append({"role": "user", "content": user_message})
        placeholder_text = random.choice(thinking_texts)
        st.session_state.chat_messages.append({"role": "assistant", "content": placeholder_text})
        st.rerun()

    # Replace placeholder with real reply
    if st.session_state.chat_messages and st.session_state.chat_messages[-1]["content"] in thinking_texts:
        # Keep the placeholder visible in chat
        placeholder_text = st.session_state.chat_messages[-1]["content"]

        with st.spinner(placeholder_text):  # <-- show the same friendly placeholder in spinner
            reply = generate_chatbot_reply(st.session_state.chat_messages[-2]["content"])

        # Swap out the placeholder with the real reply
        st.session_state.chat_messages[-1]["content"] = reply or "⚠️ Couldn't generate a response this time."

        st.rerun()

    


    # Display chat history
    for msg in st.session_state.chat_messages:
        if msg["role"] == "assistant":
            st.markdown(
                f"<div style='background:#00314a; color:#fff; padding:8px; border-radius:10px; margin:6px 0;'>{msg['content']}</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"<div style='background:#2b2b2b; color:#fff; padding:8px; border-radius:10px; margin:6px 0; text-align:right;'>{msg['content']}</div>",
                unsafe_allow_html=True,
            )








