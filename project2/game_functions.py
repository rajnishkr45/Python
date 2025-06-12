from random import randint


def generate_number():
    return randint(1, 51)


def check_the_guess(user_guess, actual_answer):
    if user_guess == actual_answer:
        return "You guess it correct, Congratulations"

    elif user_guess > actual_answer:
        return "Your guess is bigger than answer, samller number please"

    elif user_guess < actual_answer:
        return "Your guess is smaller than answer, bigger number please"

    else:
        return "Invalid Input"


def store_game_data(username, number_of_guess):
    with open("project2/game_data.txt", "a") as f:
        f.write(f"{username} : {str(number_of_guess)}\n")
    return "Game result saved successfully"


def fetch_data():
    with open("project2/game_data.txt", "r") as f:
        result = f.readlines()
        return result


def decide_winner(old_score, old_user, new_score):
    if old_score == new_score:
        return "Score tie"

    elif old_score < new_score:
        return "Your score is the highest, Congratulations !"

    elif old_score > new_score:
        return f"{old_user}, has the highest score!"
