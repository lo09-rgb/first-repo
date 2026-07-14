class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        print(f"{val} pushed to stack.")

    def pop(self):
        if not self.stack:
            print("Stack Underflow! Stack is empty.")
        else:
            val = self.stack.pop()
            print(f"{val} popped from stack.")

    def peek(self):
        if not self.stack:
            print("Stack is Empty!")
        else:
            print(f"Top element is: {self.stack[-1]}")

    def display(self):
        if not self.stack:
            print("Stack is Empty!")
        else:
            print("Stack elements (Top to Bottom):", end=" ")
            # Print from top (end of list) to bottom (start of list)
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i], end=" ")
            print()

    def is_empty(self):
        if not self.stack:
            print("Stack is Empty.")
        else:
            print("Stack is NOT Empty.")

def main():
    st = Stack()
   
    while True:
        print("\n--- Stack Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Is Empty")
        print("6. Exit")
       
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            try:
                value = int(input("Enter value to push: "))
                st.push(value)
            except ValueError:
                print("Invalid input! Please enter an integer.")
        elif choice == 2:
            st.pop()
        elif choice == 3:
            st.peek()
        elif choice == 4:
            st.display()
        elif choice == 5:
            st.is_empty()
        elif choice == 6:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")
main()
