import sqlite3

def init_db():
    with sqlite3.connect("connect4.db") as db:
        cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)
    db.commit()

def register_user(username, password):
    with sqlite3.connect("connect4.db") as db:
        cursor = db.cursor()
    cursor.execute("INSERT INTO users(username, password) VALUES (?, ?)", (username, password))
    db.commit()

def login_user(username, password):
    with sqlite3.connect("connect4.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return cursor.fetchone()
