"""
Raw SQL query functions for the Q&A app.
"""
from db.connection import get_connection
from typing import Any, Dict, List, Optional

def fetch_all_subjects() -> List[str]:
    sql = "SELECT DISTINCT subject FROM questions WHERE end_effective_date IS NULL OR end_effective_date > datetime('now')"
    with get_connection() as conn:
        rows = conn.execute(sql).fetchall()
    return [row["subject"] for row in rows]

def fetch_categories_by_subject(subject: str) -> List[str]:
    sql = "SELECT DISTINCT category FROM questions WHERE subject = ? AND (end_effective_date IS NULL OR end_effective_date > datetime('now'))"
    with get_connection() as conn:
        rows = conn.execute(sql, (subject,)).fetchall()
    return [row["category"] for row in rows]

def insert_user(user_id: str, name: str) -> None:
    sql = "INSERT OR IGNORE INTO users (id, name, created_at) VALUES (?, ?, datetime('now'))"
    with get_connection() as conn:
        conn.execute(sql, (user_id, name))
        conn.commit()

def insert_question(subject: str, category: str, difficulty: int, question_text: str, model_answer: str, asked_at: str, source: Optional[str], end_effective_date: Optional[str], created_by: Optional[str]) -> int:
    sql = """
        INSERT INTO questions (subject, category, difficulty, question_text, model_answer, asked_at, source, end_effective_date, created_by)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    with get_connection() as conn:
        cur = conn.execute(sql, (subject, category, difficulty, question_text, model_answer, asked_at, source, end_effective_date, created_by))
        conn.commit()
        return cur.lastrowid

def insert_answer(question_id: int, user_id: str, answer_text: str, correctness: int, completeness: int, clarity: int, depth: int, overall_grade: str, feedback: str, answered_at: str, graded_at: Optional[str], session_id: Optional[str]) -> int:
    sql = """
        INSERT INTO answers (question_id, user_id, answer_text, correctness, completeness, clarity, depth, overall_grade, feedback, answered_at, graded_at, session_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    with get_connection() as conn:
        cur = conn.execute(sql, (question_id, user_id, answer_text, correctness, completeness, clarity, depth, overall_grade, feedback, answered_at, graded_at, session_id))
        conn.commit()
        return cur.lastrowid

def log_user_activity(user_id: str, activity_type: str, activity_data: Optional[str]) -> None:
    sql = "INSERT INTO user_activity_log (user_id, activity_type, activity_data, created_at) VALUES (?, ?, ?, datetime('now'))"
    with get_connection() as conn:
        conn.execute(sql, (user_id, activity_type, activity_data))
        conn.commit()
