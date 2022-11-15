logo = """
 _____________________
|  _________________  |
| | Lucas Gab Winter| | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)


def sum_(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": sum_, "-": subtract, "*": multiply, "/": divide}


def check_number(number):
    try:
        number = float(number)
        return number
    except ValueError:
        number = check_number(input("Please type a valid number:\n"))
        return number


def check_input(op_symbol):
    if op_symbol == "+" or op_symbol == "-" or op_symbol == "*" or op_symbol == "/":
        return op_symbol
    else:
        op_symbol = check_input(input("Please type a valid operation:   + - * /  \n"))
        return op_symbol


def continue_(answer):
    aux = input("Press 'y' to continue calculating, press 'n' to start"
                " a new calculation or press anything else to exit"
                " the program\n")
    if aux == "n":
        calculator()
    if aux == "y":
        return new_calculation(answer)
    else:
        return


def calculator():
    num1 = (input("What is the first number?\n"))
    num1 = check_number(num1)
    for key in operations:
        print(key)
    op_symbol = input("What operation do you wanna do?\n")
    op_symbol = check_input(op_symbol)
    num2 = (input("What is the second number?\n"))
    num2 = check_number(num2)
    answer = operations[op_symbol](num1, num2)
    print(f"{num1} {op_symbol} {num2} = {answer}")
    continue_(answer)


def new_calculation(answer):
    for key in operations:
        print(key)
    op_symbol = input("chose another operation.\n")
    op_symbol = check_input(op_symbol)
    next_num = input("what is the next number?\n")
    next_num = check_number(next_num)
    next_answer = operations[op_symbol](answer, next_num)
    print(f"{answer} {op_symbol} {next_num} = {next_answer}")
    answer = next_answer
    continue_(answer)


calculator()
