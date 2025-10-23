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
    print("Player 1 score: ", score1)
    print("Player 2 score: ", score2)
    #determine the winner
    if(score1 >= 50):
        winner = 1
    elif(score2 >= 50):
        winner = 2
    print("Congratulations Player", winner,". You WIN!")
    print("Thanks for Playing!")
def takeTurn(): #returns players decision and information
    rollOrHold = input("Roll(r)\Hold(h)?: ") #also check if it is valid
    rollOrHold = rollOrHold.lower()
    if (rollOrHold == "r" or rollOrHold == "h"):
        return rollOrHold
    else:
        takeTurn()
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
    if (score1 <50 or score2 <50):
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
    print("Player 1 score: ", score1)
    print("Player 2 score: ", score2, "\n")
    resetTurnValues()
def winner(): #print winner text and give option to restart
    print("Player 1 score: ", score1)
    print("Player 2 score: ", score2, "\n")
    #determine the winner
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
    winner()
    
main()



#//////////////////////////////////////////////////////////////////////


#import a random module
import random

#declare variables
score1 = 0
score2 = 0
maxRollCount = 0

#output the heading
print("Let's Play the Pig Game!")
print("=======GOOD LUCK========")

turn = random.randint(1,2)   #determine who's first turn is it

#a while loop that continues till one of the players reaches 50 points
while(score1 < 50 and score2 < 50):
    #output the scores
    print("Player 1 score: ", score1)
    print("Player 2 score: ", score2)
    print()
    
    turnTotal = 0   #set turnTotal to 0 in the beggining of each round
    rollCount = 0   #count the number of rolls

    
    while(decision != "h"):   #loop that continues till player decision == h or rolled == 1
        rollCount +=1
        rolled = random.randint(1,6)   #declare rolled value
        print("Roll: ", rolled)   #print rolled value
        
        if(rolled != 1):   #if rolled is not 1, add rolled to turnTotal and ask for decision again
            turnTotal += rolled
            print("Turn total: ", turnTotal)
            decision = input("Roll(r)\Hold(h)?: ")
            
        elif(rolled == 1):   #if rolled is 1, turnTotal is 0 and end the loop
            turnTotal = 0
            print("Turn total: ", turnTotal)
            break
        
    if(decision == "h" or rolled == 1):   #add points to a player, switch turn and output the score
        if(turn == 1):
            score1 += turnTotal
            turn = 2  
        elif(turn == 2):
            score2 += turnTotal
            turn = 1
    
    #check for the largest number of rolls by a player
    if(maxRollCount < rollCount):
        maxRollCount = rollCount

#output the final score and maxRollCount
print('The max number of rolls by a player: ', maxRollCount)
print("Player 1 score: ", score1)
print("Player 2 score: ", score2)

#determine the winner
if(score1 >= 50):
    winner = 1
elif(score2 >= 50):
    winner = 2

print("Congratulations Player", winner,". You WIN!")

print("Thanks for Playing!")
















