History_File = "history.txt"

def show_history():
    file = open(History_File, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No History Found!")
    elif len(lines) != 0:
        for line in reversed(lines):
            print(line.strip())
        file.close()
    else:
        print("File Openning Error!")
    return None

def clear_history():
    file = open(History_File, 'w')
    file.close()
    print("File Cleared Successfully!")
    return None

def save_to_history(equation , result):
    file = open(History_File, 'a')
    file.write(equation + ' = ' + str(result) + "\n")
    file.close()
    return None

def calculate(user_input):
    parts = user_input.split() #split on the basis of white space by default
    if len(parts) != 3:
        print("Invalid Input! Use the following format: number operator number (e.g: 7 + 6).")
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Can't divide by zero")
            return
        result = num1 / num2
    elif op == '%':
        if num2 == 0:
            print("Can't divide by zero to get reminder")
            return
        result = num1 % num2
    elif op == '**':
        result = num1 ** num2
    else:
        print("Invalid Operator: Use only + - * / % **.")
        return
    
    if int(result) == result:
        result = int(result)

    print("Result: ", result)
    save_to_history(user_input, result)

def main():
    print("--- --- --- ---  SIMPLE CALCULATOR  --- --- --- ---")
    print("Operations (+ - * / % **), History, Clear or Exit\n") 

    while True:
        user_input = input("Enter calculation(+ - * / % **) or command(history, clear, exit): ")
        if user_input == "exit":
            print("Goodbye!")
            return
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input) 

main()