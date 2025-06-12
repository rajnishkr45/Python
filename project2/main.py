import game_functions

print("\n\n")
username = input("Enter your name: ")
print(
    f"\n------------ Welcome to perfect guess game {username.lower()} ! ------------\n"
)


print("""\n------------ Rules of game ------------\n
      1. Computer will guess the number between 1 and 51
      2. You have to guess the number 
      3. The less number of attempts the better score
      4. There will be global winner based on past records\n
      """)

attempts = 0

guess = game_functions.generate_number()

inp = input("Enter 5 to start the game: ")

if int(inp) == 5:
    user_input = int(input("Enter the guess: "))
else:
    print("You entered invalid key, start the game again !")
    exit()

while guess != user_input and attempts != 5:
    print(game_functions.check_the_guess(user_input, guess))

    attempts += 1
