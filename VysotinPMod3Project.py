#Authors: Pavlo Vysotin, Brice Moeller  

#import random module
import random

rolled = 0
potentialScore = 0
score1 = 0
score2 = 0
winner = 0
currentPlayersTurn = 0

def welcome():
    global score1, score2, currentPlayersTurn
    print("Let's Play the Pig Game!")
    print("=======GOOD LUCK========")
    printScore()
    currentPlayersTurn = random.randint(1,2)
    print("It is player", currentPlayersTurn, "'s turn:")

def printScore():
    print("Player 1 score: ", score1)
    print("Player 2 score: ", score2, "\n")
    
def takeTurn(): #returns players decision and information
    rollOrHold = input("Roll(r)\Hold(h)?: ").lower()
    
    while (rollOrHold != "r" and rollOrHold != "h"):
        rollOrHold = input("Roll(r)\Hold(h)?: ") #also check if it is valid
    return rollOrHold
        
def diceRoll(): #rolls random number, part of players decision
    global rolled, potentialScore
    rolled = random.randint(1,6) #declare rolled value
    rolled = int(rolled)
    print("Roll: ", rolled)  
    if (rolled != 1):
        potentialScore += rolled
        print("Turn total: ",potentialScore, "\n")
        return True
    else:
        return False
        
def resetTurnValues(): #reset on game restart or turn change
    global potentialScore
    potentialScore = 0
    
def switchTurn(): #swap player controls
    global currentPlayersTurn 
    if (score1 <50 and score2 <50):
        printScore()
        if(currentPlayersTurn == 1):
            currentPlayersTurn = 2
        else:
            currentPlayersTurn = 1
        print("It is player", currentPlayersTurn, "'s turn:")
        
def addScore(): #turn total
    global currentPlayersTurn, score1, score2
    if(currentPlayersTurn == 1):
        score1 += potentialScore
    else:
        score2 += potentialScore
    resetTurnValues()
    
def end(): #print winner text and give option to restart
    global score1, score2, winner
    printScore()
    if(score1 >= 50):
        winner = 1
    elif(score2 >= 50):
        winner = 2
    print("Congratulations Player", winner,". You WIN!")
    print("Thanks for Playing!")
    
def main(): #intro, while loop, outro,
    global rolled, potentialScore, score1, score2, winner
    rolled = 0
    potentialScore = 0
    score1 = 0
    score2 = 0
    winner = 0
    
    #intro
    welcome()
    #while loop()
    while(score1 <50 and score2 <50): #scores < 50
        if (takeTurn() == "r"):
            if (diceRoll()): #if dice roll is not 1
                continue
            else: #if dice roll is 1    
                resetTurnValues()
                switchTurn()
        else:
            addScore()
            switchTurn()
    #outro
    end()
    
main()

