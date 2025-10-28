import sqlite3
import hashlib

conn = sqlite3.connect("staffdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS staffdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)

""")

username1 , password1 = "Azer1215", hashlib.sha256("Bananafromsky1089".encode()).hexdigest()
username2 , password2 = "zander", hashlib.sha256("zander_xm".encode()).hexdigest()
username3 , password3 = "Andrew", hashlib.sha256("andrew1000".encode()).hexdigest()
username4 , password4 = "James", hashlib.sha256("jamesbrain80".encode()).hexdigest()

cur.execute("INSERT INTO staffdata (username, password) VALUES (?, ?)", (username1,password1))
cur.execute("INSERT INTO staffdata (username, password) VALUES (?, ?)", (username2,password2))
cur.execute("INSERT INTO staffdata (username, password) VALUES (?, ?)", (username3,password3))
cur.execute("INSERT INTO staffdata (username, password) VALUES (?, ?)", (username4,password4))

conn.commit()