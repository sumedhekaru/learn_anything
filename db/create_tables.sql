-- Users table (id = email address)
CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY, -- user's email address
    name TEXT NOT NULL,
    created_at DATETIME NOT NULL
);

-- Questions table
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    category TEXT NOT NULL,
    difficulty INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    model_answer TEXT,
    asked_at DATETIME NOT NULL,
    source TEXT,
    end_effective_date DATETIME,
    created_by TEXT,
    FOREIGN KEY (created_by) REFERENCES users(id)
);

-- Answers table
CREATE TABLE IF NOT EXISTS answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL,
    user_id TEXT NOT NULL,
    answer_text TEXT,
    correctness INTEGER,
    completeness INTEGER,
    clarity INTEGER,
    depth INTEGER,
    overall_grade TEXT,
    feedback TEXT,
    answered_at DATETIME NOT NULL,
    graded_at DATETIME,
    session_id TEXT,
    FOREIGN KEY (question_id) REFERENCES questions(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
