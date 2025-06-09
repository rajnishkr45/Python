# write a program to update the soce of a user when he brakes the old high score

import random


def game():
    print("You are playing the game...")
    return random.randint(1, 100)


new_score = game()

with open("highscore.txt", "r") as high_score:
    old_score = int(high_score.read()) #fetch old high score


if(old_score <= new_score): #compared new score with old high score
    print(f"New High Score: {new_score}")
    with open("highscore.txt", "w") as high_score:
        high_score.write(str(new_score)) # if new score is greater than old one then update it
else:
    print(f"Current Score: {new_score}\n High Score: {old_score}")
        

