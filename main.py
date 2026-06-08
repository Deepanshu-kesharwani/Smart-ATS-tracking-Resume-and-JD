import streamlit as st
import os
import json
import PyPDF2 as pdf
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()



client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    default_headers={
        "HTTP-Referer": os.getenv("SITE_URL", "http://localhost"),
        "X-OpenRouter-Title": os.getenv("SITE_NAME", "Smart ATS"),
    },
)

def get_openrouter_response(input_text):
    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",   # change to any OpenRouter model slug you want
        messages=[
            {
                "role": "user",
                "content": input_text
            }
        ],
        temperature=0.2
    )
    return response.choices[0].message.content

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of tech field, software engineering, data science,
data analyst and big data engineer. Your task is to evaluate the resume based
on the given job description.

You must consider the job market is very competitive and you should provide
best assistance for improving the resumes. Assign the percentage matching based
on JD and the missing keywords with high accuracy.

Resume:
{text}

Job Description:
{jd}

I want the response in one single string having the structure:
{{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
"""

# Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")

jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        prompt = input_prompt.format(text=text, jd=jd)

        try:
            response = get_openrouter_response(prompt)
            st.subheader("ATS Result")
            st.write(response)

            # Optional: try to display as JSON
            try:
                parsed = json.loads(response)
                st.json(parsed)
            except:
                pass

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please upload a resume PDF.")