import streamlit as st
import requests

def fetch_jobs_original(skill, location="India"):
    app_id = st.secrets["api"]["adzuna_app_id"]
    app_key = st.secrets["api"]["adzuna_app_key"]

    if not skill.strip():  # ✅ prevent empty queries
        return []

    url = f"https://api.adzuna.com/v1/api/jobs/in/search/1"
    params = {
        "app_id": app_id,
        "app_key": app_key,
        "results_per_page": 10,
        "what": skill,
        "where": location,
        "content-type": "application/json"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        st.error(f"Failed to fetch job listings. ({response.status_code})")
        return []


def fetch_jobs(skill, location="India"):
    app_id = st.secrets["api"]["adzuna_app_id"]
    app_key = st.secrets["api"]["adzuna_app_key"]

    if not skill.strip():
        return []

    url = f"https://api.adzuna.com/v1/api/jobs/in/search/1"
    params = {
        "app_id": app_id,
        "app_key": app_key,
        "results_per_page": 10,
        "what": skill,
        "where": location,
        "content-type": "application/json"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        st.error(f"Failed to fetch job listings. ({response.status_code})")
        return []