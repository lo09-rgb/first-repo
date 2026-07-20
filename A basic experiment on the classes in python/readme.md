# Student Grading System

A simple Python OOP program to calculate a student's total marks, average, and grade based on 5 subject scores.

## Features

- Takes student roll number, name, and marks in 5 subjects as input
- Calculates **Total** and **Average** marks
- Assigns a **Grade** based on average:

| Average Range | Grade |
|----------------|-------|
| 90 – 100       | A     |
| 80 – 90        | B     |
| 70 – 80        | C     |
| 60 – 70        | D+    |
| Below 60       | F     |

- Displays a formatted summary of student details

## Class Overview: `Student`

**Attributes**
- `RollNo`, `Name` — student identity
- `M1`–`M5` — marks in 5 subjects
- `Total`, `Average`, `Grade` — computed results

**Methods**
- `Calculate_Total()` — sums all 5 marks
- `Calculate_Average()` — divides total by 5
- `Find_Grade()` — assigns grade based on average
- `Display()` — prints roll no, name, total, average, and grade

## How to Run

```bash
python student.py
```

You'll be prompted to enter:
1. Roll number
2. Name
3. Marks in 5 subjects (M1–M5)

The program then prints the calculated total, average, and grade.

## Example

```
Enter Roll No: 101
Enter Name: Aayusshman
Enter Marks 1: 88
Enter Marks 2: 92
Enter Marks 3: 79
Enter Marks 4: 85
Enter Marks 5: 90

Student Details
Roll No : 101
Name     : Aayusshman
Total    : 434
Average  : 86.8
Grade    : B
```

## Note

Grade boundaries currently use `>` on the lower bound, so an exact average of 60, 70, 80, or 90 falls into the *lower* grade band (e.g., an average of exactly 90 gives grade **B**, not A). Adjust the comparisons in `Find_Grade()` if you want inclusive lower bounds instead.
