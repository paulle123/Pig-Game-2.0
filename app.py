from flask import Flask, render_template, request
from pigDiceGame import PigDiceGame

app = Flask(__name__)
app.secret_key = "donthackpls" 

game = PigDiceGame() # create one instance of the game
winCheck = False # global variable that checks whether there's a winner; saves from game oversaving

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
    global winCheck # makes sure that the same game doesn't get saved multiple times
    rolled = None # keeps track of currrent number; use instead of last_roll

    # check if user pressed on button
    if request.method == "POST":
        action = request.form.get("action") # gets value from HTML form; button name or hidden input

        # if action is "roll" or "hold", assign message with either of functions from pigDiceGame
        if action == "roll":    
            game.roll()
        elif action == "hold":
            game.hold()

        # check if someone won
        winner = game.check_winner()
        if winner:  # prints message and save results
            if winCheck == False:
                game.save_result()
                winCheck = True
        # resets the values and starts game again
        if action == "reset":
            winCheck = False
            game.reset()
        
        if action == "homepage":
            winCheck = False
            game.reset()
            return home()
    # show the webpage and allows to use variables below
    return render_template(
        "play.html",
        rolled=game.last_roll,
        score1=game.score1,
        score2=game.score2,
        turn=game.current,
        potential=game.potential,
        winner=game.winner,
    )

# history page
@app.route('/history')
def history():
    data = game.getLastFiveResults()

    return render_template("history.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
