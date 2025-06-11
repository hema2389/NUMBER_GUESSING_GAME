# 🎲 Number Guessing Game

A fun and simple Python CLI game where the player tries to guess a randomly generated number between 1 and 100.

## 🚀 Features

- Random number generation using `random.randint()`
- User input with guess feedback: too high or too low
- Keeps track of the number of attempts
- Allows graceful exit with `"exit"` command
- Input validation for non-integer guesses

## 🛠️ Technologies Used

- Python 3
- Standard Library (`random`, `input`, `print`)

## 📦 How to Run

1. Make sure you have Python installed.
2. Save the script as `number_game.py`.
3. Run it from your terminal or IDE:

```bash
python number_game.py

##Sample Gameplay
🎯 New Game Started! Guess a number between 1 and 100 or type 'exit' to quit.
Enter your guess: 50
Too low.. Guess a little higher.
Enter your guess: 75
Too high.. Guess a little lower.
Enter your guess: 68
🎉 Hurray! You found the number 68 in 3 attempts.

## Project Structure
number_game/
├── number_game.py
└── README.md

## ✅ Author
Made using Python as part of a learning journey in mini projects.
