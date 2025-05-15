from pathlib import Path
from db.connection import get_connection, DB_PATH

SCHEMA_PATH = Path(__file__).parent / "create_tables.sql"

def initialize_database():
    """Initializes the SQLite database with all tables if they don't exist."""
    with open(SCHEMA_PATH, "r") as f:
        schema_sql = f.read()
    with get_connection() as conn:
        conn.executescript(schema_sql)

if __name__ == "__main__":
    initialize_database()
    print(f"Database initialized at {DB_PATH}")
