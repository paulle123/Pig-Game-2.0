# app.py
from flask import Flask, render_template, request
from pigDiceGame import PigDiceGame

app = Flask(__name__)
app.secret_key = "secret123"

game = PigDiceGame()    # create one instance of the game

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

@app.route("/intro")
def intro(): 
    return render_template("intro.html")
    
@app.route("/play", methods=["GET", "POST"])
def play():     # defines a function that runs every time someone visits or interacts with /play

    rolled = None   # keeps track of currrent number; use instead of last_roll

    if request.method == "POST":            # check if user pressed on button
        action = request.form.get("action") # gets value from HTML form; button name or hidden input

        # if action is "roll" or "hold", assign message with either of functions from pigDiceGame
        if action == "roll":    
            game.roll()
        elif action == "hold":
            game.hold()

        # check if someone won
        winner = game.check_winner()
        if winner:  # prints message and save results
            game.save_result()

        if action == "reset":   # resets the values and starts game again
            game.reset()
        
        if action == "homepage":
            game.reset()
            return home()

    return render_template(     # show the webpage and allows to use variables below
        "play.html",
        rolled=game.last_roll,
        score1=game.score1,
        score2=game.score2,
        turn=game.current,
        potential=game.potential,
        winner=game.winner,
    )

@app.route('/history')
def history():
    data = game.getLastFiveResults()

    return render_template("history.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
