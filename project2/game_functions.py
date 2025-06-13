from random import randint


def generate_number():
    return randint(1, 100)


def check_the_guess(user_guess, actual_answer):
    if user_guess == actual_answer:
        return 0  # correct guess

    elif user_guess > actual_answer:
        return 1  # user answer greater than actual answer

    elif user_guess < actual_answer:
        return -1  # user answer is less than actual answer

    else:
        return 404  # Invalid input


def store_game_data(username, number_of_guess):
    with open("project2/game_data.txt", "a") as f:
        f.write(f"{username} : {str(number_of_guess)}\n")
