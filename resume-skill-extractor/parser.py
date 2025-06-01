import os
import pdfplumber
import google.generativeai as genai
from dotenv import load_dotenv
import re

# Load .env and Gemini API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model (Flash is fastest & free-tier friendly)
model = genai.GenerativeModel("gemini-2.0-flash")

def extract_pure_json(text):
    # Remove triple backticks and optional language labels
    json_text = re.sub(r"```(json)?", "", text)
    return json_text.strip("` \n")

def extract_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return " ".join(page.extract_text() or "" for page in pdf.pages)

def extract_with_llm(text):
    prompt = f"""
Extract the following fields from the resume text below:
- Full name
- Email
- Phone number
- Skills (comma-separated)
- Work experience (summarize all entries with role, company, and duration)

Resume Text:
{text}

Return result strictly in this JSON format without wrapping in triple backticks or markdown formatting:
{{
  "name": "...",
  "email": "...",
  "phone": "...",
  "skills": "...",
  "experience": "..."
}}

"""

    response = model.generate_content(prompt)
    cleaned = extract_pure_json(response.text)
    return cleaned

