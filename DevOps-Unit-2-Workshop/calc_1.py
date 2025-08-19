
def addition (x,y):
    return x + y
def multiplication (x,y):
    return x * y
def subtraction (x,y):
    return x - y
def division (x,y):
    return x / y

try:
    while True:
        operator = input("Which operation you want to perform (+, -, *, /) or 'q' to quit: ").strip() 
        if operator.lower() == 'q':
            break
        if operator not in ['+','-','*','/']:
            print("Invalid operator entered")
            continue # go back to the start of the while loop
        
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                break  # got valid numbers, exit this inner loop
            except ValueError:
                print("Invalid number. Please enter numeric values.")
        
        # Perform calculation        
        if operator == "+":
            print(addition(num1,num2))
        elif operator == "-":
            print(subtraction(num1,num2))
        elif operator == "*":
            print(multiplication(num1,num2))
        elif operator == "/":
            if operator == "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:    
                    print(division(num1,num2))

except ValueError:
    print("Invalid input")

