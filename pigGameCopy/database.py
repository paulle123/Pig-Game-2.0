#database.py
import sqlite3
from datetime import datetime

class Database:
# Step 1 Create Data Base and connection
    def __init__(self, db_name="pig_game.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        
# Step 2 Create the data that needs to be stored
    def createTable(self):
        query = """
        CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY,
        savedTime TEXT,
        winner TEXT,
        results TEXT
        )
        """
        try:
            
            self.conn.execute(query)
        except Exception as e:
            print(e)

# Step 3 Add(record) data to a database
    def saveGame(self, savedTime, winner, results):
        query = "INSERT INTO history (savedTime, winner, results) VALUES (?, ?, ?)"
        try:
            with self.conn:
                self.conn.execute(query, (savedTime, winner, results))
        except Exception as e:
            print(e)
                       


# Step 4 Access the data
    def getLastFiveRows(self):
        self.cursor.execute("SELECT * FROM history ORDER BY id DESC LIMIT 5")
        rows = self.cursor.fetchall()
        return list(reversed(rows)) # Print them in normal ascending or

# Step 5 Close Data
    def close(self):
        self.conn.close()