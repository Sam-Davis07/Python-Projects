from arts import logo

def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mutliply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mutliply,
    "/" : divide
}


def calculator():
    
    print(logo)
    num1 = float(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        cal_symbol = input("Pick an operator from the line above: ")

        num2 = float(input("What is the second number?: "))
    
        cal_func = operations[cal_symbol]   # num1 {oprator} num2
    
        answer = cal_func(num1,num2)
    
        print(f"{num1} {cal_symbol} {num2} = {answer}")
    
        if input(f"Want to continue calculation with {answer} type 'y' or 'n': ").lower() == 'y':
        
            num1 = answer
    
        else:
            should_continue = False
                    
calculator()