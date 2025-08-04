import streamlit as st
import subprocess
import sys
from skill_matcher import match_skills
from utils import open_json_file, export_to_excel
from resume_parser import parse_resume
from skill_set import MASTER_SKILLS 

OUTPUT_JSON_FILE = "final_jobs_list.json"

st.set_page_config(page_title="Fit4JobRole", layout="wide")
st.title("🔍 Fit4JobRole – Get Matched to the Right Job")

with st.sidebar:
    st.header("Upload Your Resume")
    uploaded_file = st.file_uploader("Choose PDF or DOCX", type=["pdf", "docx"])

    st.markdown("**OR**")
    manual_skills = st.multiselect(
        "Enter your skills (comma-separated)",
        options=MASTER_SKILLS,
        help="Start typing (e.g., 'pyt' for Python, 'aws' for AWS...)"
    )

    job_role = st.text_input("Job Role", value="Python Developer")
    location = st.text_input("Location", value="Hyderabad")
    max_pages = st.slider("Pages to search", 1, 5, 1)

if st.button("Find Jobs"):
    if uploaded_file:
        resume_skills = parse_resume(uploaded_file)
    elif manual_skills:
        resume_skills = manual_skills
    else:
        st.warning("Please upload a resume or enter skills manually.")
        st.stop()
    
    with st.spinner("🔄 Searching Jobs ..."):

        try:
            job_search_scripts = ["naukri_jobs_search.py", "microsoft_jobs_search.py"]
            for script_name in job_search_scripts:
                s_process = subprocess.run(
                    [sys.executable, script_name, "--role", job_role, "--location", location, "--pages", str(max_pages), 
                        "--output", OUTPUT_JSON_FILE],
                    timeout=60,
                    capture_output=True,
                    text=True
                )

                job_portal_name = script_name.replace("_jobs_search.py","")
                if s_process.returncode != 0:
                    st.error(f"❌ {job_portal_name} Job Search failed!")
                    st.code(s_process.stderr)
                else:
                    st.success(f"✅ {job_portal_name} Subprocess completed successfully.")


        except Exception as e:
            st.error(f"⏱️ Something wrong while finding jobs. Exception: {e}")

        jobs = open_json_file(OUTPUT_JSON_FILE)

        enriched_jobs = []

        for job in jobs:
            skill_match = match_skills(resume_skills, job["description"])
            job.update(skill_match)
            enriched_jobs.append(job)

            # removing the job descriptions because there is too much text and not needed in excel file
            del job["description"] 

        st.success(f"✅ Found {len(enriched_jobs)} jobs and matching your skills done")

        for job in enriched_jobs:
            st.markdown(f"### [{job.get('title')}]({job.get('job_link')})")
            st.write(f"**Company:** {job.get('company_name')}")
            st.write(f"📍 {job.get('location')} | 💰 {job.get('salary')} ")
            st.write(f"**Matched Skills:** {', '.join(job.get('matched_skills'))}")
            st.write(f"**Missing Skills:** {', '.join(job.get('missing_skills'))}")
            st.write(f"🧠 Match Score: **{job.get('match_percentage')}%**")
            st.markdown("---")

        try:
            st.download_button("📤 Download Excel", export_to_excel(enriched_jobs), file_name="MatchedJobs.xlsx")
        except:
            st.warning("⚠️ Exception while downloading file")


