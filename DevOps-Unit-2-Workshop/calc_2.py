
def addition (x,y):
    return x + y
def multiplication (x,y):
    return x * y
def subtraction (x,y):
    return x - y
def division (x,y):
    return x / y
def operator_map(op):
    # convert 'x' to '*', keep others as-is
    return "*" if op == "x" else op

with open("oplist.txt", "r") as file:
    lines = file.read().splitlines()

total = 0 
for line in lines:
    parts = line.split()
    #if len(parts) != 4 or parts[0].lower() != "calc":
    #    print(f"Ignoring invalid line: {line}")
    #    continue

    op = operator_map(parts[1])
    try:
        num1 = float(parts[2])
        num2 = float(parts[3])
    except ValueError:
        print(f"Invalid numbers in line: {line}")
        continue

    if op not in ['+', '-', '*', '/']:
        print(f"Invalid operator in line: {line}")
        continue

    if op == '+':
        result = addition(num1, num2)
    elif op == '-':
        result = subtraction(num1, num2)
    elif op == '*':
        result = multiplication(num1, num2)
    elif op == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = division(num1, num2)
    total += result
print(f"Sum of numbers: {total}")