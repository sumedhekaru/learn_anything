from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from db.queries import fetch_all_subjects, fetch_categories_by_subject, insert_question
import os
import openai
from datetime import datetime

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class QuestionRequest(BaseModel):
    subject: str
    category: str
    difficulty: int

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head><title>Learn Anything Q&A</title></head>
        <body>
            <h1>Hello, World!</h1>
            <p>Welcome to the Learn Anything Q&A App (FastAPI + Jinja2).</p>
        </body>
    </html>
    """

@app.get("/subjects", response_model=list)
def get_subjects():
    """Get all available subjects."""
    subjects = fetch_all_subjects()
    return subjects

@app.get("/categories/{subject}", response_model=list)
def get_categories(subject: str):
    """Get all categories for a given subject."""
    categories = fetch_categories_by_subject(subject)
    if not categories:
        raise HTTPException(status_code=404, detail="Subject not found or has no categories.")
    return categories

@app.post("/generate_question")
def generate_question(req: QuestionRequest):
    """Generate a conceptual question using OpenAI LLM. No calculation-based questions for physics."""
    prompt = f"""
Generate a conceptual, subject-agnostic question in the field of {req.subject} (category: {req.category}, difficulty: {req.difficulty}). 
- The question should test conceptual understanding, not rote memorization or calculation.
- If the subject is physics, do NOT generate calculation-based or numerical questions; focus on qualitative, conceptual topics only.
- Provide a model answer as well.
Return the result as:
Question: <question text>
Model Answer: <model answer>
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400,
            temperature=0.7
        )
        content = response.choices[0].message.content
        # Parse response
        lines = content.split("\n")
        question_text = ""
        model_answer = ""
        for line in lines:
            if line.lower().startswith("question:"):
                question_text = line.partition(":")[2].strip()
            elif line.lower().startswith("model answer:"):
                model_answer = line.partition(":")[2].strip()
        if not question_text or not model_answer:
            raise ValueError("Could not parse question/model answer from LLM response.")
        # Store in DB
        asked_at = datetime.utcnow().isoformat()
        qid = insert_question(
            subject=req.subject,
            category=req.category,
            difficulty=req.difficulty,
            question_text=question_text,
            model_answer=model_answer,
            asked_at=asked_at,
            source="llm",
            end_effective_date=None,
            created_by=None
        )
        return {"id": qid, "question": question_text, "model_answer": model_answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate question: {str(e)}")
