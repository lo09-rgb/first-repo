# 🎯 Guess the Number Game (Python)

A simple command-line **Guess the Number** game built using Python. The program generates a random number, and the player keeps guessing until the correct number is entered.

## 📌 Features

* Generates a random number using Python's `random` module.
* Accepts user input from the terminal.
* Uses **functions** to organize the code.
* Demonstrates **recursion** by repeatedly asking the user for another guess after an incorrect attempt.
* Displays a success message when the correct number is guessed.

---

## 🧠 Concepts Practiced

* Functions
* Recursion
* Conditional Statements (`if` / `else`)
* User Input (`input()`)
* Random Number Generation
* Function Calls

---

## 📂 Project Structure

```text
guess_the_number.py
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the source code.
3. Open a terminal in the project folder.
4. Run the program:

```bash
python guess_the_number.py
```

---

## 🎮 Sample Output

```text
guess the number game
Hey please enter the number between [1:30]: 12
please try again bro

Hey please enter the number between [1:30]: 25
please try again bro

Hey please enter the number between [1:30]: 18
yes the correct number is 18
```

---

## 💡 How It Works

1. The program generates a random number.
2. The user is asked to guess the number.
3. If the guess is correct, the program congratulates the user.
4. If the guess is incorrect, the function calls itself (recursion) to ask for another guess.
5. This continues until the correct number is entered.

---

## 📚 What I Learned

While building this project, I practiced:

* Breaking a program into functions.
* Using recursion to repeat program execution.
* Taking input from the user.
* Comparing values with conditional statements.
* Generating random numbers with Python's `random` module.

I also learned that although recursion works for this project, a `while` loop is generally the preferred approach for repeated user input because it avoids creating a new function call for every incorrect guess.

---

## 🚀 Future Improvements

* Count the number of attempts.
* Give hints like **"Too High"** or **"Too Low"**.
* Handle invalid inputs using `try`/`except`.
* Add difficulty levels (Easy, Medium, Hard).
* Allow the player to play multiple rounds.
* Display the best score (fewest attempts).

---

## 🛠️ Technologies Used

* Python 3
* `random` module

---

## 👨‍💻 Author

**Aayusshman**

Learning Python, Data Structures & Algorithms, and AI/ML one project at a time.
