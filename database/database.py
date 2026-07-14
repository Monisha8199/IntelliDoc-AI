import sqlite3

conn = sqlite3.connect("database/intellidoc.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(

id INTEGER PRIMARY KEY AUTOINCREMENT,

feature TEXT,

filename TEXT,

result TEXT

)
""")

conn.commit()