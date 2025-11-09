import sqlite3

# connect (creates pig_game.db if it doesn’t exist)
conn = sqlite3.connect("pig_game.db")
cur = conn.cursor()

# create tables
cur.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    score INTEGER,
    date_played TEXT,
    FOREIGN KEY (player_id) REFERENCES players(id)
)
""")

conn.commit()
conn.close()
print("✅ Database and tables created!")
