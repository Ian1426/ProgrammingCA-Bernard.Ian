def calculator(a, b, operation):
    #Performs basic operations: add, subtract, multiply, divide.
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b 
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Division by zero error"
    else:
        return "Invalid Operation"

a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
operator = input("Enter operator: (add, subtract, multiply, divide): ").lower()

result = calculator(a, b, operator)
print("Result:", result)