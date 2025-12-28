Portfolio Website Creation using LLMs and Streamlit

This project is an AI-powered application that automatically generates a complete personal portfolio website (HTML, CSS, and JavaScript) from a resume document. Instead of manually designing a portfolio or copying content from resumes, users can upload a PDF or DOCX resume and instantly receive a downloadable website bundle.

The application is built using Streamlit for the frontend interface and Google’s Gemini model (via LangChain) for content and code generation.

Problem Statement

Creating a personal portfolio website is time-consuming for many students and early-career professionals. While resumes already contain structured information such as skills, experience, projects, and education, converting this information into a well-designed website usually requires frontend expertise and manual effort.

Additionally:

Resume formats vary widely
Copy-pasting content is error-prone
Non-developers struggle with HTML/CSS/JS

This project solves that gap by automating the entire process.

Solution Overview

The application follows a simple and deterministic pipeline:

1.User uploads a resume (PDF or DOCX)
2.Resume text is extracted programmatically
3.Extracted text is passed to an LLM with strict output formatting rules

The LLM generates:

1.index.html,
2.style.css,
3.script.js,

All files are bundled into a ZIP file
User downloads the ready-to-use portfolio website

The model is explicitly instructed to output code in a fixed delimiter-based format, allowing the application to reliably split and store each file.

Tech Stack

1.Python,
2.Streamlit – UI and user interaction,
3.LangChain – LLM orchestration,
4.Google Gemini (gemini-2.5-flash-lite) – Code generation,
5.PyPDF – PDF text extraction,
6.python-docx – DOCX text extraction,
Features:Supports both PDF and DOCX resumes,No manual text input required,Generates clean frontend code automatically

Downloadable ZIP output

Lightweight and easy to deploy
Suitable for demos, portfolios, and rapid prototyping

Limitations

*Resume PDFs with complex layouts may produce noisy text
*Output parsing relies on strict delimiters
*Generated websites are static (no backend)
*Not production-hardened (intended for MVP and learning use cases)

These are known and acceptable trade-offs for the current scope.

Setup Instructions

1.Clone the repository

2.Install dependencies:
pip install -r requirements.txt

3.Add your Google Gemini API key to .env:
gemini=YOUR_API_KEY

4.Run the app:
streamlit run app.py
