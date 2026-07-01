# Password Generator

Generates a password from a person's **name** and **city**, guaranteed to meet a set of complexity rules.

## How it works

1. Takes `name` and `city` as input (spaces are stripped, so multi-word entries like `"Anil Kumar"` work fine).
2. Extracts **every 3rd letter from the name**, starting from the beginning (i.e. the 3rd, 6th, 9th, ... letters).
3. Extracts **every 2nd letter from the city**, starting from the beginning (i.e. the 2nd, 4th, 6th, ... letters).
4. Combines those letters into a base password.
5. Checks the base against the required rules and adds a random character for any rule not already satisfied:
   - at least 1 uppercase letter
   - at least 1 lowercase letter
   - at least 1 number
   - at least 1 special character
6. Pads with random characters if the result is still under 8 characters.
7. Shuffles the final character list so the structure isn't predictable.

## Requirements

- Python 3

No external packages are needed — only the standard library (`random`, `string`).

## Usage

```bash
python3 password_generator.py
```

You'll be prompted for input:

```
Enter your name: anushya
Where do you live?: chennai
Your Password is: :yhIau4n
```

Because random characters are used to satisfy missing conditions and the final result is shuffled, the output will differ on every run — but it will always satisfy all of the rules below.

## Rules satisfied by every generated password

| # | Rule |
|---|------|
| 1 | Includes every 3rd letter from the name |
| 2 | Includes every 2nd letter from the city |
| 3 | At least 8 characters long |
| 4 | At least 1 uppercase letter |
| 5 | At least 1 lowercase letter |
| 6 | At least 1 number |
| 7 | At least 1 special character |

## Using it as a module

```python
from password_generator import generate_password

password = generate_password("anushya", "chennai")
print(password)
```

## Notes

- "Every 3rd/2nd letter starting from the beginning" is interpreted as 1-indexed positions (3rd, 6th, ... for the name; 2nd, 4th, ... for the city). If your use case expects 0-indexed positions instead, change `name[2::3]` to `name[0::3]` and `city[1::2]` to `city[0::2]` in `password_generator.py`.
- If the name and city are very short, most of the password will come from the random padding step rather than the extracted letters.
