import sqlite3
from settings import DB_NAME, SQL_FILE

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

with open(SQL_FILE, "r") as f:
    cursor.executescript(f.read())
    conn.commit()
