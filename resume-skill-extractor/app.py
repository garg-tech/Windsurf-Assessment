import streamlit as st
from parser import extract_text, extract_with_llm
from storage import save_result, load_all_resumes
import json

st.set_page_config(page_title="Resume Skill Extractor", layout="wide")
st.title("📄 Resume Skill Extractor")

# Upload PDF
uploaded_file = st.file_uploader("Upload a resume (PDF)", type=["pdf"])

if uploaded_file:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ Uploaded successfully!")

    text = extract_text(uploaded_file.name)
    json_response = extract_with_llm(text)
    try:
        data = json.loads(json_response)
    except Exception as e:
        st.error("❌ LLM response was not valid JSON.")
        st.code(json_response)
        st.exception(e)  # Helpful for debugging
        st.stop()

    st.subheader("📋 Extracted Summary")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**👤 Name:** {data.get('name', 'N/A')}")
        st.markdown(f"**✉️ Email:** {data.get('email', 'N/A')}")
        st.markdown(f"**📞 Phone:** {data.get('phone', 'N/A')}")
    with col2:
        st.markdown("**🛠 Skills:**")
        for skill in data.get("skills", "").split(","):
            st.markdown(f"- {skill.strip()}")

    st.markdown("**💼 Work Experience:**")
    st.markdown(data.get("experience", "N/A"))

    save_result(data)

# Sidebar - Resume Filtering
st.sidebar.subheader("🔍 Browse Stored Resumes")
if st.sidebar.button("Load Resumes"):
    resumes = load_all_resumes()
    skill_tags = set()
    for r in resumes:
        for s in r.get("skills", "").split(","):
            skill_tags.add(s.strip())

    selected = st.sidebar.multiselect("Filter by Skill", sorted(skill_tags))
    for r in resumes:
        resume_skills = [s.strip() for s in r.get("skills", "").split(",")]
        if all(s in resume_skills for s in selected):
            st.sidebar.markdown(f"### {r['name']}")
            st.sidebar.markdown(f"- Email: {r['email']}")
            st.sidebar.markdown(f"- Skills: {r['skills']}")
            st.sidebar.markdown("---")
