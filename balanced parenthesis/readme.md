# Check Balanced Parentheses Using Stack

A Python program that checks whether an expression containing `()`, `{}`, and `[]` is balanced, using a Stack data structure.

## Problem Statement

Given a string `S` consisting only of the characters `(`, `)`, `{`, `}`, `[`, `]`, determine whether the brackets are balanced.

An expression is **balanced** if:
- Every opening bracket has a matching closing bracket of the same type.
- Brackets are closed in the correct (properly nested) order.

## Input Format

A single line containing string `S`.

## Output Format

- `Balanced` — if the string is valid.
- `Not Balanced` — if the string is invalid.

## Constraints

- 1 ≤ Length of `S` ≤ 1000
- String contains only bracket characters.

## Approach

1. Initialize an empty stack.
2. Traverse the string character by character.
3. If the character is an opening bracket (`(`, `{`, `[`), push it onto the stack.
4. If the character is a closing bracket (`)`, `}`, `]`):
   - If the stack is empty, the expression is **Not Balanced** (extra closing bracket).
   - Pop the top element and check if it matches the corresponding opening bracket. If not, the expression is **Not Balanced**.
5. After traversing the string:
   - If the stack is empty, all brackets matched correctly → **Balanced**.
   - If the stack is not empty, there are unmatched opening brackets → **Not Balanced**.

This works because a stack's LIFO (Last In, First Out) behavior naturally mirrors how nested brackets must close in reverse order of how they were opened.

## Time and Space Complexity

- **Time Complexity:** O(n), where n is the length of the string — each character is processed once.
- **Space Complexity:** O(n) in the worst case, when all characters are opening brackets and get pushed onto the stack.

## How to Run

```bash
python balanced_parentheses.py
```

Then type the expression when prompted, and press Enter.

### Example

```
Input:  ()[]{}
Output: Balanced
```

```
Input:  ([)]
Output: Not Balanced
```

## Test Cases

| Input                | Output       |
|-----------------------|--------------|
| `()[]{}`             | Balanced     |
| `([)]`               | Not Balanced |
| `()`                 | Balanced     |
| `(]`                 | Not Balanced |
| `{[()]}`             | Balanced     |
| `(((`                | Not Balanced |
| `)))`                | Not Balanced |
| `[{]}`               | Not Balanced |
| `[]`                 | Balanced     |
| `([{}])`             | Balanced     |
| `(((((((())))))))`   | Balanced     |
