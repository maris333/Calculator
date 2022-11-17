
# Calculator application
def calculator():
    print("Welcome to calculator!")
    end = ""
    while end != "exit":
        val = ""
        val2 = ""
        operation = ""
        val = number_validation(val, "Please enter the first number: ")
        val2 = number_validation(val2, "Please enter the second number: ")
        while not (operation == "+" or operation == "-" or operation == "*" or operation == "/"):
            operation = input("Choose +, -, * or / : ")
        if operation == "+":
            add(val, val2)
        elif operation == "-":
            subtract(val, val2)
        elif operation == "*":
            multiply(val, val2)
        elif operation == "/":
            divide(val, val2)
        end = input("Type 'exit' to end the program or whatever else to continue: ")


def number_validation(val, message):
    while not val.isdigit():
        val = input(message)
    return val


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


if __name__ == '__main__':
    calculator()

