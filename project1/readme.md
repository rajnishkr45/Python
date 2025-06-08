# 🐍 Snake Water Gun Game 🎮

A fun command-line game of **Snake-Water-Gun** built using modular Python files. This project demonstrates basic Python concepts like functions, conditionals, loops, random choice, and modularity through file organization.

---

## 📁 Project Structure

```
snake-water-gun/
│
├── main.py             # Main file to run the game
├── machine.py          # Contains machineChoice() using random module
└── game_data.py        # Stores global data like choices and scores
```

---

## 🎯 Game Rules

* **Snake drinks Water** → Snake wins 🐍 > 💧
* **Gun kills Snake** → Gun wins 🔫 > 🐍
* **Water sinks Gun** → Water wins 💧 > 🔫

---

## 🚀 How to Play

1. Clone or download this repo.
2. Make sure you have Python installed (`>= 3.x`).
3. Run the game:

```bash
python main.py
```

4. Enter your name.
5. Choose:

   * `s` for Snake
   * `w` for Water
   * `g` for Gun
6. Continue or exit after each round.

---

## 🧠 Features & Concepts Used

* `random.choice()` for machine's decision
* Conditional logic to decide winner
* Modular code with separate Python files
* Dynamic score tracking using dictionary
* User input and game loop control

---

## 📷 Example Output

```
------------------ Welcome to Snake Gun game -----------------

Enter your name: Rajnish

---------------- Rules of GAME --------------

        1. Snake drinks water : Snake wins
        2. Gun kills snake : Gun wins
        3. Water sinks gun : Water wins
        ** To EXIT the game Enter any number except 5
        ** To CONTINUE the game press 5

Enter 5 to start the game: 5
Enter your choice (s/w/g): s

Your choice was SNAKE and Computer choice was WATER
    You won, Congratulations!

Enter 5 to continue or any other number to quit: 2

------------------- GAME RESULT -------------------

Total matches played: 1
Rajnish won, Congratulations!
Machine: 0
Rajnish: 1
```

---

<!-- ## 📌 To-Do / Future Improvements

* Add GUI using `tkinter` or `pygame`
* Store scores across sessions
* Add animations or sound effects -->


## 🧑‍💻 Author

**Rajnish Kumar**

* GitHub: [@rajnishkr45](https://github.com/rajnishkr45)
* LinkedIn: [@rajnish45](https://www.linkedin.com/in/rajnish45)

---
