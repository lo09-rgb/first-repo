# 🔤 Anagram Checker (Python)

A simple Python program that checks whether two words or phrases are **anagrams** of each other.

An **anagram** is formed by rearranging the letters of one word or phrase to create another while using every letter exactly once.

## ✨ Features

- Accepts two words or phrases as input.
- Ignores spaces while comparing.
- Case-insensitive comparison.
- Returns whether the inputs are anagrams or not.
- Clean and beginner-friendly implementation using Python functions.

## 📖 How It Works

1. Takes two inputs from the user.
2. Removes all spaces from both strings.
3. Converts both strings to lowercase.
4. Sorts the characters of both strings.
5. Compares the sorted lists.
6. Prints whether they are anagrams.

## 🧠 Logic Used

```python
cleaned_str1 = str1.replace(" ", "").lower()
cleaned_str2 = str2.replace(" ", "").lower()

return sorted(cleaned_str1) == sorted(cleaned_str2)
```

### Why Sorting Works

If two strings are anagrams, they contain exactly the same characters with the same frequencies.

For example:

```
listen  -> eilnst
silent  -> eilnst
```

Since the sorted characters match, the words are anagrams.

---

## ▶️ Example

### Input

```
Enter the first phrase or word: Listen
Enter the second phrase or word: Silent
```

### Output

```
"Listen" and "Silent" are anagrams!
```

---

### Input

```
Enter the first phrase or word: Hello
Enter the second phrase or word: World
```

### Output

```
"Hello" and "World" are NOT anagrams.
```

---

## 📂 Project Structure

```
anagram-checker/
│
├── anagram_checker.py
└── README.md
```

---

## ⏱️ Time Complexity

Sorting each string takes:

```
O(n log n)
```

where **n** is the length of the string.

Overall Time Complexity:

```
O(n log n)
```

Space Complexity:

```
O(n)
```

because Python's `sorted()` creates new lists.

---

## 🚀 Future Improvements

- Ignore punctuation marks.
- Handle numbers and special characters.
- Implement a frequency-count approach using dictionaries for **O(n)** time complexity.
- Add a GUI using Tkinter or PyQt.
- Create a web version using Flask or Django.

---

## 📚 Concepts Practiced

- Functions
- String Manipulation
- User Input
- Conditional Statements
- Sorting
- Boolean Return Values
- Time Complexity Analysis

---

## 🛠️ Built With

- Python 3

---

## 🎯 Learning Outcome

This project demonstrates how simple preprocessing (removing spaces and normalizing case) combined with sorting can efficiently determine whether two strings are anagrams. It is an excellent beginner project for understanding string operations, functions, and algorithmic thinking in Python.
