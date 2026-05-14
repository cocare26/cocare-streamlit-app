import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "app.db")


def get_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        user_id TEXT,
        region TEXT,
        message TEXT,
        language TEXT,
        intent TEXT,
        intent_confidence REAL,
        sentiment TEXT,
        sentiment_score REAL,
        prediction INTEGER,
        issue_type TEXT,
        network_problem INTEGER,
        notification_type TEXT,
        display_channel TEXT,
        escalation INTEGER,
        reason TEXT,
        repeat_count INTEGER,
        area_issue_count INTEGER
    )
    """)

    conn.commit()
    conn.close()


init_db()
