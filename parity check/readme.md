# Parity Checker

A small Python script that checks whether a number and the sum of its digits share the same parity (both even or both odd).

## What it does

1. Asks the user to enter a number.
2. Checks if the number is even or odd.
3. Adds up the digits of the number.
4. Checks if that digit sum is even or odd.
5. Compares the two parities — if they match, it's a "parity"; if not, it isn't.

## Usage

```bash
python parity_checker.py
```

You'll be prompted:
```
Enter the number you want to check the parity for:
```
Type an integer and press Enter.

## Example

For input `123`:
- `123` is odd.
- Digit sum: `1 + 2 + 3 = 6`, which is even.
- Since odd ≠ even, it is **not** a parity match.

## Known issues (as currently written)

This script has a few bugs that will cause incorrect or misleading output — worth fixing before relying on it:

- **`if` blocks have no `else`**: the "odd", "sum is odd", and "not a parity" lines print unconditionally every time, regardless of the actual result.
- **`paritycheck(n)` is called with an undefined `n`** at the bottom of the script, and the function ignores its `n` parameter anyway, re-reading input from the user inside the function instead. The call should just be `paritycheck()`.
- **Redundant slicing**: `new_list[0:len(new_list)+1]` is equivalent to just `new_list`.

## Suggested fix structure

```python
if n % 2 == 0:
    print('Even number as input')
else:
    print('Odd number as input')
```
(and similarly for the other two `if` statements)

## Requirements

- Python 3.x
