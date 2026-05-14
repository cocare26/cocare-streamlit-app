import sqlite3

DATABASE_NAME = "database/cocare.db"


def connect_db():

    conn = sqlite3.connect(DATABASE_NAME)

    return conn

def create_tables():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            full_name TEXT NOT NULL,

            phone TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            role TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            sender TEXT,

            message TEXT,

            sentiment TEXT,

            intent TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    conn.commit()

    conn.close()

if __name__ == "__main__":

    create_tables()

    print("Database Created Successfully")

