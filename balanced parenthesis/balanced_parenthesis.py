def is_balanced(expression):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            top = stack.pop()
            if top != matching[char]:
                return False

    return len(stack) == 0


def main():
    S = input().strip()
    if is_balanced(S):
        print("Balanced")
    else:
        print("Not Balanced")


if __name__ == "__main__":
    main()
