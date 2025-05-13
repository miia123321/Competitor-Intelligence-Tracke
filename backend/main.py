from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import docx
import spacy
import tempfile
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Allow all CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# --- CV Upload Endpoint ---
def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

@app.post("/upload-cv/")
async def upload_cv(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(tmp_path)
    elif file.filename.endswith(".docx"):
        text = extract_text_from_docx(tmp_path)
    else:
        return {"error": "Unsupported file type"}

    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

    # Mock entity filters
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    education = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "EDUCATION"]]
    experience = [ent.text for ent in doc.ents if ent.label_ == "WORK_OF_ART"]

    return {
        "filename": file.filename,
        "text": text[:1000],
        "entities": entities,
        "skills": skills,
        "education": education,
        "experience": experience,
    }

# --- Job Matching Endpoint ---
MOCK_JOBS = [
    {
        "title": "Software Engineer Intern",
        "company": "Tech Innovations",
        "skills": ["Python", "Machine Learning", "Teamwork"],
        "education": ["Johns Hopkins University", "Computer Science"],
        "link": "https://example.com/job1"
    },
    {
        "title": "Data Analyst",
        "company": "Health Insights",
        "skills": ["Data Analysis", "R", "Statistics"],
        "education": ["Statistics", "Mathematics"],
        "link": "https://example.com/job2"
    },
    {
        "title": "Business Analyst",
        "company": "Finance Group",
        "skills": ["Excel", "Business Analysis", "Communication"],
        "education": ["Economics", "Business"],
        "link": "https://example.com/job3"
    },
]

class Qualifications(BaseModel):
    skills: List[str]
    education: List[str]
    experience: List[str]

@app.post("/match-jobs/")
async def match_jobs(qualifications: Qualifications):
    matches = []
    for job in MOCK_JOBS:
        skill_overlap = len(set(job["skills"]) & set(qualifications.skills))
        edu_overlap = len(set(job["education"]) & set(qualifications.education))
        score = skill_overlap * 2 + edu_overlap
        if score > 0:
            matches.append({"job": job, "score": score})
    matches.sort(key=lambda x: x["score"], reverse=True)
    return {"matches": matches}


