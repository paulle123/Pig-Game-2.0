# pigDiceGame.py

# import modules
import random
import time
from database import Database

class PigDiceGame:
    def __init__(self):
        self.db = Database()                # connect to DB only once
        self.score1 = 0
        self.score2 = 0
        self.potential = 0
        self.current = random.randint(1, 2)
        self.winner = None
        self.last_roll = None                # store last dice value rolled

    def roll(self):      # roll the dice
        self.last_roll = random.randint(1, 6)   
        if self.last_roll != 1:                 
            self.potential += self.last_roll    
            return f"Rolled {self.last_roll}!"  
        else:                                   
            self.potential = 0                  
            self.switch_turn()                  
            return f"Rolled 1"                  

    def hold(self):         # hold current turn and add to score
        if self.current == 1:
            self.score1 += self.potential
        else:
            self.score2 += self.potential
        self.potential = 0
        self.switch_turn()

    def switch_turn(self):    # switch between players
        self.current = 1 if self.current == 2 else 2

    def check_winner(self):    # check if either player reached 50
        if self.score1 >= 50:
            self.winner = "Player 1"
        elif self.score2 >= 50:
            self.winner = "Player 2"
        return self.winner

    def save_result(self):    # store the game result in the database
        if self.winner:
            result = f"{self.score1}/{self.score2}"
            self.db.saveGame(time.ctime(), self.winner, result)

    def reset(self):    # start a new game
        self.score1 = 0
        self.score2 = 0
        self.potential = 0
        self.winner = None
        self.current = random.randint(1, 2)
        self.last_roll = None

    def getLastFiveResults(self):
        """Fetch and format last 5 game results from the database."""
        rows = self.db.getLastFiveRows()
        if not rows:
            return "<p>No past games found.</p>"

        table = "<table border='1' cellspacing='0' cellpadding='8' style='margin:auto;'>"
        table += "<tr><th>Date & Time</th><th>Winner</th><th>Result</th></tr>"

        for row in rows:
            savedTime, winner, results = row[1], row[2], row[3]
            table += f"<tr><td>{savedTime}</td><td>{winner}</td><td>{results}</td></tr>"

        table += "</table>"
        return table
