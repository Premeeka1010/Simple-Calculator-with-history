import re

HISTORY_FILE = "history.txt"
HISTORY_FILE_MAX_SIZE = 1000000

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No history found!")
            else:
                print("\n--- Calculation History ---")
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found!")

def clear_history():
    with open(HISTORY_FILE, 'w') as file:
        pass
    print("History cleared!")

def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(equation + " = " + str(result) + "\n")

def is_valid_expression(expr):
    # Allow only numbers, operators, parentheses, spaces
    pattern = r'^[\d\s+\-*/%().**]+$'
    return re.fullmatch(pattern, expr) is not None

def calculate(user_input):
    # Replace multiple spaces with single space
    expression = user_input.replace('**', '^').replace('^', '**')  # Allow `^` as shortcut for power
    if not is_valid_expression(expression):
        print("Error: Invalid characters in expression.")
        return None

    try:
        result = eval(expression)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return result
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as e:
        print("Error in calculation:", e)
    
    return None

def main():
    print('--- SIMPLE CALCULATOR ---')
    print("Supports multiple numbers & operators: e.g., 4 + 5 + 6 - 3 * 2 / 1")
    print("Operators: +  -  *  /  %  ** or ^ (for power)")
    print("Commands: 'history', 'clear', 'exit'\n")

    while True:
        user_input = input('Enter your expression: ').strip()
        if user_input.lower() == 'history':
            show_history()
        elif user_input.lower() == 'clear':
            clear_history()
        elif user_input.lower() == 'exit':
            print('Goodbye!')
            break
        else:
            result = calculate(user_input)
            if result is not None:
                print("Result:", result)
                save_to_history(user_input, result)

main()
