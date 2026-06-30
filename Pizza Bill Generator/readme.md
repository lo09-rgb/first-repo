# 🍕 Pizza Billing System

## Overview

The **Pizza Billing System** is a simple command-line application built using Python. It allows users to order different types of pizzas, customize them with additional items, calculates the final bill by applying GST and discounts, and generates a random bill number.

This project was created to practice Python fundamentals such as conditional statements, user input, arithmetic operations, and program flow.

---

## Features

* Choose between **Normal** and **Deluxe** pizzas.
* Select **Veg** or **Non-Veg** options.
* Add optional extras:

  * Extra Cheese
  * Extra Toppings
  * Water Bottles
  * Ketchup Packets
  * Soft Drinks
  * Carry Bag (Takeaway)
* Automatic bill generation.
* Random bill number generation.
* GST calculation (18%).
* Discount applied based on the total bill.
* Displays the final payable amount.

---

## Pizza Prices

| Pizza Type |  Veg | Non-Veg |
| ---------- | ---: | ------: |
| Normal     | ₹300 |    ₹400 |
| Deluxe     | ₹600 |    ₹800 |

---

## Additional Charges

| Item           |    Price |
| -------------- | -------: |
| Extra Cheese   |     ₹100 |
| Extra Toppings |     ₹100 |
| Water Bottle   | ₹20 each |
| Ketchup Packet |  ₹5 each |
| Soft Drink     | ₹75 each |
| Carry Bag      |      ₹20 |

---

## Technologies Used

* Python 3
* Random Module

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/pizza-billing-system.git
```

2. Navigate to the project folder.

```bash
cd pizza-billing-system
```

3. Run the program.

```bash
python pizza.py
```

---

## Sample Workflow

```
Choose Pizza
        ↓
Choose Veg / Non-Veg
        ↓
Add Cheese
        ↓
Add Toppings
        ↓
Add Water Bottles
        ↓
Add Ketchup
        ↓
Add Soft Drinks
        ↓
Takeaway?
        ↓
Generate Bill
        ↓
Apply GST
        ↓
Apply Discount
        ↓
Display Final Amount
```

---

## Concepts Practiced

* Variables
* User Input
* Nested `if` Statements
* Arithmetic Operations
* Conditional Logic
* String Formatting (f-strings)
* Random Number Generation
* Billing Calculations

---

## Future Improvements

* Reduce repetitive code using functions.
* Implement input validation.
* Use loops to improve the ordering process.
* Store menu items using dictionaries.
* Generate a detailed itemized bill.
* Save bills to a text or PDF file.
* Add a graphical user interface (GUI).

---

## Author

**Aayusshman**

This project was built as a Python practice project to strengthen problem-solving and programming fundamentals.
