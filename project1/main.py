# main.py

from game_data import scores
from machine import machineChoice


def printScore(score, userName):
    print(f"Machine: {score['machine']}")
    print(f"{userName}: {score[userName]}")


def updateScore(score, winner, userName):
    if winner == "user":
        score[userName] += 1
    elif winner == "machine":
        score["machine"] += 1
    printScore(score, userName)


def decideWinner(machinechoice, userchoice, score, userName):
    if userchoice == machinechoice:
        print("Game tied, both prediction was same!")

    elif userchoice == "s" and machinechoice == "w":
        print("Your choice was SNAKE and Computer choice was WATER")
        print("\tYou won, Congratulations!")
        updateScore(score, "user", userName)

    elif userchoice == "s" and machinechoice == "g":
        print("Your choice was SNAKE and Computer choice was GUN")
        print("\tYou lost, Oops!")
        updateScore(score, "machine", userName)

    elif userchoice == "w" and machinechoice == "s":
        print("Your choice was WATER and Computer choice was SNAKE")
        print("\tYou lost, Oops!")
        updateScore(score, "machine", userName)

    elif userchoice == "w" and machinechoice == "g":
        print("Your choice was WATER and Computer choice was GUN")
        print("\tYou won, Congratulations!")
        updateScore(score, "user", userName)

    elif userchoice == "g" and machinechoice == "w":
        print("Your choice was GUN and Computer choice was WATER")
        print("\tYou lost, Oops!")
        updateScore(score, "machine", userName)

    elif userchoice == "g" and machinechoice == "s":
        print("Your choice was GUN and Computer choice was SNAKE")
        print("\tYou won, Congratulations!")
        updateScore(score, "user", userName)
    else:
        print("Invalid input, start the game again!")
        exit()


# ------------------- GAME START --------------------

print("\n------------------ Welcome to Snake Gun game -----------------\n")

userName = input("Enter your name: ")
scores[userName] = 0  # Initialize user's score

print("""
---------------- Rules of GAME -------------- \n
\t1. Snake drinks water : Snake wins\n
\t2. Gun kills snake : Gun wins\n
\t3. Water sinks gun : Water wins\n
\t** To EXIT the game Enter any number except 5\n
\t** To CONTINUE the game press 5\n """)

rounds = 0
j = int(input("Enter 5 to start the game: "))

print("------------------- GAME START --------------------\n")

if j == 5:
    while True:
        userchoice = input("Enter your choice (s/w/g): ").lower()
        print()
        answer = machineChoice()
        decideWinner(answer.lower(), userchoice, scores, userName)
        rounds += 1

        i = input("Enter 5 to continue or any other number to quit: ")
        if i != "5":
            break

# ------------------- RESULT --------------------

print("\n------------------- GAME RESULT -------------------\n")
print(f"Total matches played: {rounds}\n")

if scores["machine"] > scores[userName]:
    print("Machine won, Better luck next time!")
elif scores["machine"] < scores[userName]:
    print(f"{userName} won, Congratulations!")
else:
    print("Game tied!")

printScore(scores, userName)
