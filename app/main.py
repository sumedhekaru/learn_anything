from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import HTTPException
from db.queries import fetch_all_subjects, fetch_categories_by_subject

app = FastAPI()

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
