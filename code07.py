stack = []

def is_empty():
    return len(stack) == 0

def push(element):
    stack.append(element)
    print("Element", element, "pushed onto the stack.")


def pop():
    if is_empty():
        print("Stack is empty. Cannot perform pop operation.")
    else:
        element = stack.pop()
        print("Element", element, "popped from the stack.")

def display_stack():
    if is_empty():
        print("Stack is empty.")
    else:
        print("Stack:")
        for i in stack:
            print(i)

while True:
    print("\nSTACK OPERATIONS")
    print("1. Push an element")
    print("2. Pop an element")
    print("3. Display stack")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        element = input("Enter the element to push: ")
        push(element)
    elif choice == '2':
        pop()
    elif choice == '3':
        display_stack()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid options (1-4).")