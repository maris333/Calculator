# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def calculator():
    val = input("Please enter a number: ")
    val2 = input("Please enter a second number: ")
    while not val.isdigit() & val2.isdigit():
        print("Choose a number")
        val = input("Please enter a number: ")
        val2 = input("Please enter a second number: ")
    action = input("Choose +, -, * or /: ")
    while not (action == "+" or action == "-" or action == "*" or action == "/"):
        action = input("Choose again  +, -, * or / : ")
    if action == "+":
        add(val, val2)
    elif action == "-":
        subtract(val, val2)
    elif action == "*":
        multiply(val, val2)
    elif action == "/":
        divide(val, val2)
    print("Finished")


def add(val, val2):
    print(int(val) + int(val2))


def subtract(val, val2):
    print(int(val) - int(val2))


def multiply(val, val2):
    print(int(val) * int(val2))


def divide(val, val2):
    try:
        print(int(val) / int(val2))
    except ZeroDivisionError:
        print("Do not divide by 0!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculator()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
