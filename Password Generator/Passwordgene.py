import random
import string


def generate_password(name, city):
    name = name.replace(" ", "")
    city = city.replace(" ", "")

    name_letters = name[2::3]
    city_letters = city[1::2]

    password_chars = list(name_letters + city_letters)

    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/\\"

    if not any(c.isupper() for c in password_chars):
        password_chars.append(random.choice(string.ascii_uppercase))

    if not any(c.islower() for c in password_chars):
        password_chars.append(random.choice(string.ascii_lowercase))

    if not any(c.isdigit() for c in password_chars):
        password_chars.append(random.choice(string.digits))

    if not any(c in special_chars for c in password_chars):
        password_chars.append(random.choice(special_chars))

    all_chars = string.ascii_letters + string.digits + special_chars
    while len(password_chars) < 8:
        password_chars.append(random.choice(all_chars))

    random.shuffle(password_chars)

    return "".join(password_chars)


if __name__ == "__main__":
    name = input("Enter your name: ")
    city = input("Where do you live?: ")
    password = generate_password(name, city)
    print(f"Your Password is: {password}")
