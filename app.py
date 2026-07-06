from flask import Flask, render_template, request, session, redirect, url_for
from pigDiceGame import PigDiceGame
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-key") 

def load_game():
    if "game" in session:
        return PigDiceGame.from_dict(session["game"])
    return PigDiceGame()

def save_game(game):
    session["game"] = game.to_dict()

# homepage
@app.route("/")
def home():
    monologue = (
        "Welcome to the Pig Game!<br>"
        "The rules are simple:<br>"
        "1. Who gets 50 points first, wins<br>"
        "2. You can either roll or hold the dice<br>"
        "3. The sum of the rolls is the turn total<br>"
        "4. If you roll 1, you don't get any points and it becomes the opponent's turn<br>"
        "5. If you hold, you secure the turn's points and it becomes the opponent's turn"
    )
    return render_template("index.html", monologue=monologue)

# loading screen page
@app.route("/intro")
def intro(): 
    return render_template("intro.html")

# play page
@app.route("/play", methods=["GET", "POST"])
def play(): # defines a function that runs every time someone visits or interacts with /play
    game = load_game()

    # check if user pressed on button
    if request.method == "POST":
        action = request.form.get("action") # gets value from HTML form; button name or hidden input

        # if action is "roll" or "hold", assign message with either of functions from pigDiceGame
        if action == "roll":    
            game.roll()
        elif action == "hold":
            game.hold()
        elif action == "reset":
            game.reset()
            session["saved"] = False
        elif action == "homepage":
            game.reset()
            session["saved"] = False
            save_game(game)
            return redirect(url_for("home"))
        
        if game.check_winner() and not session.get("saved"):
            game.save_result()
            session["saved"] = True

        save_game(game)
        # Post/Redirect/Get
        return redirect(url_for("play"))
    
    return render_template(
        "play.html",
        rolled=game.last_roll,
        score1=game.score1,
        score2=game.score2,
        turn=game.current,
        potential=game.potential,
        winner=game.winner,
    )

# polling
@app.route("/state")
def state():
    game = load_game()
    return game.to_dict()

# history page
@app.route('/history')
def history():
    game = load_game()
    data = game.getLastFiveResults()

    return render_template("history.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,
debug=os.environ.get("FLASK_DEBUG") == "1")