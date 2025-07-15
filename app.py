import streamlit as st
import pandas as pd
import base64
import joblib
import numpy as np
import json
from thefuzz import fuzz,process
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import io


st.set_page_config(
    page_title="SkillSpread : Level Up. Break In. Stand Out",
    page_icon="🎓",
    layout="wide"
)

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_base64 = get_base64_of_bin_file("logo.png")

st.markdown(
    f"""
    <div style='text-align: center; margin-top: -90px;'>
        <img src='data:image/png;base64,{img_base64}' width='250' style='margin-bottom: -50px';/>
        <h1 style="margin-top: 0px;">🚀 SkillSpread : Level Up. Break In. Stand Out</h1>
    </div>
    """,
    unsafe_allow_html=True
)


st.write("👋 Welcome to SkillSpread - A way you can find how to land on your dream job by finding the skills that are required for your dream job")
st.markdown("---")

data = pd.read_csv("skillspread_dataset.csv")
roles_from_data = sorted(data['job_role'].str.title().unique())

model = joblib.load("model/job_role_predictor.pkl")
vectorizer = joblib.load("model/skill_vectorizer.pkl")
job_roles = model.classes_


col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Enter Your name", placeholder="Type Here...")

with col2:
    job_role = st.selectbox("Select your desired job role:", ['Select'] + roles_from_data)

skills = st.text_area(label='Enter your skills', placeholder='separate your skills with a comma')
st.divider()

skill_normalizer = {
    "powerbi": "power bi",
    "power-bi": "power bi",
    "ms excel": "excel",
    "adv excel": "excel",
    "machinelearning": "machine learning",
    "ml": "machine learning",
    "sql": "sql",
    "js": "javascript",
    "py": "python",
    "scikit": "scikit-learn",
    "scikitlearn": "scikit-learn",
    "statistic": "statistics",
    "stat": "statistics",
    "human resource executive": "hr executive",
    "human resources executive": "hr executive",
    "git hub": "git",
    "threed modelling": "3d modelling",
    "three d modelling": "3d modelling",
    "model-deployment": "model deployment",
    "deployment": "model deployment",
    "node js": "node.js",
    "tech writing": "technical writing",
    "data pipeline": "data pipelines",
    "requirements analysis": "requirement analysis",
    "ui ux design": "ui/ux design",
    "ui-ux design": "ui/ux design",
    "ui ux": "ui/ux",
    "ui-ux": "ui/ux"
}

def normalize_skill(skill):
    return skill_normalizer.get(skill, skill)

def fuzzy_match(skill, skill_list, threshold = 65):
    match, score = process.extractOne(skill, skill_list, scorer=fuzz.token_set_ratio)
    return match if score >= threshold else None



if st.button('Analyze Skills'):
    user_skills_cleaned = [normalize_skill(skill.strip().lower()) for skill in skills.split(",")]

    try:
        user_skills_text = ", ".join(user_skills_cleaned)
        X_input = vectorizer.transform([user_skills_text])
        probas = model.predict_proba(X_input)[0]
        top_3_indices = np.argsort(probas)[::-1][:3]
        top_3_roles = [model.classes_[i] for i in top_3_indices]
    except Exception as e:
        st.error("❌ Oops! Something went wrong while predicting your job role.")
        st.caption(f"🛠️ Technical info: {e}")
        st.stop()

    if job_role == "Select":
        st.error("Please select a valid job role.")
        st.stop()

    index = data[data["job_role"] == job_role.lower()].index[0]

    core_skills = data.iat[index, 1].split(",")
    core_skills_cleaned = [normalize_skill(skill.strip().lower()) for skill in core_skills]

    optional_skills = data.iat[index, 2].split(",")
    optional_skills_cleaned = [normalize_skill(skill.strip().lower()) for skill in optional_skills]

    matching_core_skills = []
    for user_skill in user_skills_cleaned:
        matched = fuzzy_match(user_skill, core_skills_cleaned)
        if matched and matched not in matching_core_skills:
            matching_core_skills.append(matched)

    missing_core_skills = [skill for skill in core_skills_cleaned if skill not in matching_core_skills]

    matching_optional_skills = []
    for user_skill in user_skills_cleaned:
        matched = fuzzy_match(user_skill, optional_skills_cleaned)
        if matched and matched not in matching_optional_skills:
            matching_optional_skills.append(matched)

    missing_optional_skills = [skill for skill in optional_skills_cleaned if skill not in matching_optional_skills]

    # Combine matched core and optional skills
    all_matched_skills = list(set(matching_core_skills + matching_optional_skills))

    # Convert to single string
    final_user_skills_text = ", ".join(all_matched_skills)

    # Send to vectorizer + model
    X_input = vectorizer.transform([final_user_skills_text])
    probas = model.predict_proba(X_input)[0]

    
    st.markdown(f"Hi **{name}** 👋 here's your personalized report for **{job_role}**!")
    st.subheader("🧠 Core Skills Analysis")

    # Safely parse the resources JSON
    resources_raw = data.iat[index, 3]
    resources_dict = {}
    try:
        decoded_once = json.loads(resources_raw)

        # If it's still a string (i.e. encoded again), decode again
        if isinstance(decoded_once, str):
            resources_dict = json.loads(decoded_once)
        else:
            resources_dict = decoded_once

        if not isinstance(resources_dict, dict):
            raise ValueError("Final parsed result is not a dictionary.")

    except Exception as e:
        st.error(f"❌ Failed to parse skill resources: {e}")
        st.stop()

    if matching_core_skills:
        st.success(f"🎉 Skills you already have: {', '.join(matching_core_skills)}")
    else:
        st.warning("Looks like you're starting from scratch🔥 — but that's okay! Let’s build your skill set step by step.")

    if missing_core_skills:
        st.error(f"⚠️ Core skills you need to learn: {', '.join(missing_core_skills)}")
        st.subheader("📚 Learn Your Missing Core Skills")

        core_table_data = []
        for skill in missing_core_skills:
            resource = resources_dict.get(skill.strip().lower(), {})
            row = {
                "Skill": skill.title(),
                "Free": resource.get("free", "Not available"),
                "Paid": resource.get("paid", "Not available")
            }
            core_table_data.append(row)

        table_rows = ""
        for row in core_table_data:
            try:
                free_text, free_url = "Not available", "#"
                paid_text, paid_url = "Not available", "#"

                if "](" in row["Free"]:
                    free_text = row["Free"].split("](")[0][1:]
                    free_url = row["Free"].split("](")[1][:-1]

                if "](" in row["Paid"]:
                    paid_text = row["Paid"].split("](")[0][1:]
                    paid_url = row["Paid"].split("](")[1][:-1]

                table_rows += f"""
                    <tr>
                        <td>🧠 <b>{row['Skill']}</b></td>
                        <td>🎓 <a href="{free_url}" target="_blank">{free_text}</a></td>
                        <td>💰 <a href="{paid_url}" target="_blank">{paid_text}</a></td>
                    </tr>
                """
            except:
                continue

        full_html = f"""
            <style>
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
            }}
            th, td {{
                border: 1px solid #444;
                padding: 10px;
                text-align: left;
                color: white
            }}
            th {{
                background-color: #1f1f1f;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #2c2c2c;
            }}
            a {{
                color: #4da6ff;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            </style>

            <table>
                <thead>
                    <tr>
                        <th>🔍 Skill</th>
                        <th>🎓 Free Resources</th>
                        <th>💰 Paid Resources</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        """

        import streamlit.components.v1 as components

        table_height = 30 + len(core_table_data) * 50
        components.html(full_html, height=table_height, scrolling=True)



    else:
        st.success("🎯 You're already equipped with all the core skills for this role. Great job!")

    st.divider()
    st.subheader("✨ Optional Skills Analysis")
    if matching_optional_skills:
        st.success(f"💡 Optional skills that you have: {', '.join(matching_optional_skills)}")

    if missing_optional_skills:
        st.info(f"📌 Optional skills you might want to explore: {', '.join(missing_optional_skills)}")
    else:
        st.success("✅ You know all the optional skills!")

    st.info("🧩 Optional Skill resources will be added soon!😊")

    st.divider()
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔮 Predicted Role Based on Your Skills")
        # Fuzzy-matched + normalized skills
        all_matched_skills = list(set(matching_core_skills + matching_optional_skills))
        final_user_skills_text = ", ".join(all_matched_skills)
        X_input = vectorizer.transform([final_user_skills_text])
        probas = model.predict_proba(X_input)[0]

        if user_skills_cleaned:
            
            top3_idx = np.argsort(probas)[::-1][:3]

            st.success("🎯 Top 3 Predicted Roles:")
            for rank, idx in enumerate(top3_idx, start=1):
                role = job_roles[idx]
                confidence = probas[idx] * 100
                if confidence > 70:
                    label = "🔥 Highly Likely"
                elif confidence > 40:
                    label = "🌟 Good Match"
                else:
                    label = "✅ Possible Fit"
                st.success(f"**{rank}. {role}** — _{label}_")
   
        else:
            st.warning("⚠️ Please enter at least one skill to predict.")
    with col2:
        st.subheader("🚀 Personalized Guidance")

        if len(missing_core_skills) == 0:
            st.success("🎉 You have all core skills!")
            st.markdown("📌 **Next Step:** Start applying for jobs or build a portfolio project!")
        elif len(missing_core_skills) <= len(core_skills_cleaned) // 2:
            st.info("💡 You're close! Just brush up on a few more skills.")
            st.markdown("📌 **Next Step:** Focus on filling the remaining gaps.")
        else:
            st.warning("🛠️ You're at the early stage.")
            st.markdown("📌 **Next Step:** Start with foundational courses and follow a beginner roadmap.")
        # Input data
        number_core = len(matching_core_skills)
        actual_core = len(core_skills)
        number_optional = len(matching_optional_skills)
        actual_optional = len(optional_skills)
        # Calculate optional percentage
        if number_optional >= actual_optional // 2 + 1:
            optional_per = 20
        else:
            optional_per = number_optional / actual_optional * 20
        # Total percentage
        per = (number_core / actual_core * 80) + optional_per
        per = min(per, 100)
        # Custom green gradient: light green to dark green
        cmap = mcolors.LinearSegmentedColormap.from_list("green_gradient", ["#b9f6ca", "#00c853"])
        # Normalize the percentage for color mapping
        norm = mcolors.Normalize(vmin=0, vmax=100)
        main_color = cmap(norm(per))
        remaining_color = "#e0e0e0"  # Light gray for incomplete portion
        # Donut chart data
        sizes = [per, 100 - per]
        colors = [main_color, remaining_color]
        # Prepare the donut chart
        fig, ax = plt.subplots(figsize=(1.5, 1.5))  # slightly larger for clarity
        ax.pie(sizes, colors=colors, startangle=90, wedgeprops=dict(width=0.3))

        # Add transparent donut hole
        centre_circle = plt.Circle((0, 0), 0.7, fc='none')  # fc='none' ensures transparency
        ax.add_artist(centre_circle)

        # Keep chart aspect ratio
        ax.axis('equal')

        # Add % text inside donut
        ax.text(0, 0, f"{per:.0f}%", ha='center', va='center', fontsize=10, fontweight='bold', color="#2e7d32")

        # Save figure to buffer with transparent background
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=100, bbox_inches='tight', transparent=True)
        buf.seek(0)

        # Display image with transparency
        st.image(buf, width=150)  # You control size here
        st.markdown("Skills Completion Percentage")

    st.markdown("---")
    
    st.caption("⚠️ *Disclaimer:* The skill recommendations and learning resources provided are based on curated, publicly available information. While we aim for accuracy, course content or availability may change over time. Please review and choose what's best for your personal learning goals.")
    st.markdown("🙏 Thanks for using SkillBridge! 🧠 Got ideas, questions, or found a bug? [Ping me on LinkedIn](https://www.linkedin.com/in/tammana-prajitha-24a5ab298/) - I'm always open to feedback!")
