def calculator():
    print("Welcome to calculator!")
    end = ""
    while end != "exit":
        val = ""
        val2 = ""
        while not val.isdigit():
            val = input("Please enter the first number: ")
        while not val2.isdigit():
            val2 = input("Please enter the second number: ")
        action = ""
        while not (action == "+" or action == "-" or action == "*" or action == "/"):
            action = input("Choose +, -, * or / : ")
        if action == "+":
            add(val, val2)
        elif action == "-":
            subtract(val, val2)
        elif action == "*":
            multiply(val, val2)
        elif action == "/":
            divide(val, val2)
        end = input("Type 'exit' to end the program or whatever else to continue: ")


def add(val, val2):
    print("The result is: " + str(int(val) + int(val2)))


def subtract(val, val2):
    print("The result is: " + str(int(val) - int(val2)))


def multiply(val, val2):
    print("The result is: " + str(int(val) * int(val2)))


def divide(val, val2):
    try:
        print("The result is: " + str(int(val) / int(val2)))
    except ZeroDivisionError:
        print("Do not divide by 0!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculator()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
