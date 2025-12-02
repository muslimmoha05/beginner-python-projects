# 🎯 Number Guessing Game

*A simple, beginner-friendly Python project to improve logic and programming skills.*

---

## 📌 Overview

The **Number Guessing Game** is a classic beginner Python project where:

* The computer chooses a **secret number** within a range
* The player has a limited number of attempts
* The game gives hints:

  * **Too high**
  * **Too low**
* The player gets an option to **play again**
* The program includes **input validation** and prevents invalid guesses
* The secret number **excludes boundaries** for better logic practice

This project is great for learning Python essentials.

---

## 🧠 Concepts You Will Learn

This project teaches and reinforces:

### ✔ Variables

Storing values like bounds, attempts, and user guesses.

### ✔ Loops

* `while` loops for replaying the game
* Nested loops for input validation

### ✔ Conditionals

Using `if / elif / else` to compare guesses.

### ✔ Random module

Choosing a random number inside a valid range.

### ✔ Input Validation

Catching invalid numbers, incorrect ranges, and out-of-bound guesses.

### ✔ Error Handling

Using `try/except` to prevent crashes when non-numeric input is entered.

---

## 🕹 How the Game Works

1. The player chooses a **lower** and **upper** bound
2. The program checks:

   * Bounds must be valid numbers
   * Lower < Upper
   * There must be at least one valid number between them
3. The computer chooses a secret number **between them (excluding boundaries)**
4. The player gets a fixed number of attempts
5. After each guess, the game tells the player:

   * Correct! 🎉
   * Too high ⬆️
   * Too low ⬇️
   * Attempts left
6. After the attempts end, the real number is revealed
7. The player can choose to **play again**

---

## ▶️ How to Run the Game

1. Open a terminal
2. Navigate to the project folder:

   ```sh
   cd number-guessing-game
   ```
3. Run the script:

   ```sh
   python game.py
   ```

---

## 🛠 Future Improvements (Good Learning Practice)

If you want to extend the game, here are beginner-friendly ideas:

* Difficulty levels (Easy/Normal/Hard)
* Randomized number of attempts
* Scoring system
* High-score saving using a text file
* GUI version using Tkinter
* Multiplayer version
* Timer countdown

---

## 📁 File Structure

```
number-guessing-game/
│
├── game.py          # Main game script
└── README.md        # Instructions and project overview
```

---

## 🤝 Contributing

If you want to improve or add features, feel free to submit a pull request.

---

## 📜 License

This project is shared under the **MIT License**, allowing free use and modification.
