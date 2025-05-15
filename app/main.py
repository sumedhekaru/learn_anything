from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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
