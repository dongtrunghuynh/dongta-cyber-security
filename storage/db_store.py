import sqlite3
from pathlib import Path

DB_PATH = "secrets.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS secrets ( 
        service TEXT PRIMARY KEY,
        api_key TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()
    
def store_api_key(service, api_key):
    if not service or not api_key:
        return False
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""INSERT OR REPLACE INTO secrets (service, api_key) VALUES (?, ?)""", (service, api_key))
    conn.commit()
    conn.close()
    return True

def retreive_api_key(service):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""SELECT api_key FROM secrets WHERE service = ?""", (service,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

init_db()


