import streamlit as st
import os
import zipfile
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pypdf import PdfReader
from docx import Document

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

st.set_page_config(page_title="Portfolio Website Creator")
st.title("Portfolio Website Creation")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    if file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join(p.text for p in doc.paragraphs)
    return ""

prompt = ""
if uploaded_file:
    prompt = extract_text(uploaded_file)

if st.button("Generate Website") and prompt.strip():
    message = [
        (
            "system",
            """You are an expert frontend web developer.
Your task is to create a complete personal portfolio website.

STRICT OUTPUT FORMAT ONLY:

--html--
[html code]
--html--

--css--
[css code]
--css--

--js--
[javascript code]
--js--
"""
        ),
        ("user", prompt)
    ]

    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    response = model.invoke(message)
    content = response.content

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content.split("--html--")[1])

    with open("style.css", "w", encoding="utf-8") as f:
        f.write(content.split("--css--")[1])

    with open("script.js", "w", encoding="utf-8") as f:
        f.write(content.split("--js--")[1])

    with zipfile.ZipFile("website.zip", "w") as zipf:
        zipf.write("index.html")
        zipf.write("style.css")
        zipf.write("script.js")

    with open("website.zip", "rb") as f:
        st.download_button(
            "Download Website ZIP",
            data=f,
            file_name="website.zip",
            mime="application/zip"
        )
