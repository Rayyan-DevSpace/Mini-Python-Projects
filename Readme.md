# 🐍 Mini Python Projects for Learning

A clean, beginner‑friendly collection of small Python programs to practice core programming skills, logic building, and problem‑solving. Each project is intentionally simple, well‑scoped, and runnable as a standalone script.

> **Why this repo?** To help you learn by doing: write small programs, get quick feedback, and build confidence.

---

## ✅ What’s Inside

* **Calculator with History** – Perform calculations and save history for later reference.
* **Fake News Headline Generator** – Generate random, humorous “fake” headlines using simple templates.
* **Rent Calculator** – Quickly estimate monthly rent splits and totals from basic inputs.
* **Rock, Paper, Scissors** – Play the classic game vs. the computer (CLI based).
* **Tic Tac Toe (GUI)** – A simple grid‑based game using Python’s built‑in `tkinter`.
* **Word Guessing Game** – Guess a hidden word within limited attempts (like Hangman‑lite).

---

## 🗂️ Suggested Folder Structure

```
mini-python-projects/
├─ calculator_with_history/
│  └─ calculator.py
├─ fake_news_headline_generator/
│  └─ generator.py
├─ rent_calculator/
│  └─ rent_calculator.py
├─ rock_paper_scissors/
│  └─ rps.py
├─ tic_tac_toe_gui/
│  └─ tic_tac_toe.py
├─ word_guessing_game/
│  └─ word_guess.py
├─ README.md
└─ requirements.txt   # optional; currently only standard library is used
```
## 🧰 Prerequisites

* **Python 3.9+** (any recent 3.x version will work)
* No external libraries required for the current scope

  * `tkinter` ships with most standard Python installs (used for Tic Tac Toe GUI)
  * if not then  ```bash pip install tkinter  ```
  
---

## 📘 Project Details & How to Run

### 1) Calculator with History

* **What it does:** Basic arithmetic (+, −, ×, ÷); logs each operation to a history file (e.g., `history.txt`).
* **Run:**

  ```bash
  python calculator_with_history/calculator.py
  ```
* **Typical flow:** Enter an expression like `2 + 3 * 4`, view the result, choose to save history.
* **Learning focus:** Parsing input, error handling, file I/O.

### 2) Fake News Headline Generator

* **What it does:** Creates random, funny headlines by combining simple templates and word lists.
* **Run:**

  ```bash
  python fake_news_headline_generator/generator.py
  ```
* **Typical flow:** Press enter (or choose a count) to print new headlines.
* **Learning focus:** Randomness, string formatting, lists.

### 3) Rent Calculator

* **What it does:** Calculates total rent, per‑person split, and optional utilities.
* **Run:**

  ```bash
  python rent_calculator/rent_calculator.py
  ```
* **Typical flow:** Enter monthly rent, number of people, (optionally) utilities or discounts.
* **Learning focus:** Input validation, arithmetic, formatting.

### 4) Rock, Paper, Scissors (CLI)

* **What it does:** User vs. computer with win/lose/draw result.
* **Run:**

  ```bash
  python rock_paper_scissors/rps.py
  ```
* **Typical flow:** Type `rock`, `paper`, or `scissors`; see the computer’s choice and the result.
* **Learning focus:** Control flow, randomness, simple game loop.

### 5) Tic Tac Toe (GUI)

* **What it does:** 3×3 grid game with turn‑based play and win/draw detection.
* **Run:**

  ```bash
  python tic_tac_toe_gui/tic_tac_toe.py
  ```
* **Typical flow:** Click cells to mark X/O; game announces winner or draw; offers reset.
* **Learning focus:** GUI events, state management with `tkinter`.

### 6) Word Guessing Game

* **What it does:** Guess letters to reveal a hidden word within a limited number of attempts.
* **Run:**

  ```bash
  python word_guessing_game/word_guess.py
  ```
* **Typical flow:** Input letters; script shows current progress (e.g., `_ a _ _`), remaining tries, and guessed letters.
* **Learning focus:** Sets/lists, loops, user feedback.

---

## 🧪 Sample Usage (CLI examples)

```text
# Calculator with History
Expression: 12 / 4 + 5\nResult: 8.0\nSave to history? (y/n): y\nSaved to history.txt

# Rock, Paper, Scissors
Your move (rock/paper/scissors): rock\nComputer: scissors\n→ You win!

# Rent Calculator
Monthly rent: 60000\nPeople sharing: 3\nUtilities (optional): 6000\nPer person: 22000.00
```

---

## 📚 Learning Outcomes

* Python basics: variables, types, functions, modules
* Control flow: conditionals, loops, simple game logic
* Data structures: lists, sets, dictionaries
* I/O: reading user input, writing to files

## 🙌 Acknowledgements

Inspired by beginner coding challenges and classroom practice tasks. Built for learning, experimenting, and having fun with Python.
