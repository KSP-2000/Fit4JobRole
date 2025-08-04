# Fit4JobRole – Get Matched to the Right Job

**Fit4JobRole** is a smart, resume-based job finder that helps users match their resume skills with real-time job descriptions from sources like **Microsoft Careers**, **Naukri.com**.

It helps users discover roles they’re qualified for and highlights the missing skills for other roles — all through a simple Streamlit web app.

---

## Features

- Upload your resume (PDF/DOCX)
- Extracts skills from your resume automatically
- Finds jobs based on role & location
- Matches your skills with job descriptions
- Displays matching percentage & missing skills
- Download results to Excel (for sharing or tracking)

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python (Playwright, Pandas, PyPDF2, docx)
- **Job Sources**: Microsoft Careers, Naukri.com
- **Export**: Excel support via Pandas

---

## Why This Project?

Most job seekers apply blindly to jobs. This tool helps:
- Find roles you actually qualify for
- Discover what skills you’re missing
- Boost chances of selection by applying more smartly

---

## Limitations & Future Work

- Matching is currently based on keyword comparison, not deep NLP and as for now more keywords can improve matching efficiency
- Scoring logic can be improved using AI/LLMs

---

## How to Run the App

```bash
git clone https://github.com/KSP-2000/Fit4JobRole.git
cd Fit4JobRole
pip install -r requirements.txt

# Install Playwright dependencies
playwright install

# Run the Streamlit app
streamlit run main.py
```


## Made by

Kelothu Shivaprasad

Aspiring Software Developer
