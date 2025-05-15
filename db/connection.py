import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "qna_app.db"


def get_connection():
    """Returns a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Enables dict-like access to rows
    return conn
