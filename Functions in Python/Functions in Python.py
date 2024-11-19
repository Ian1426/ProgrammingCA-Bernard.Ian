#Greet a user
def greet_user(name):
    return f"Hello, {name}! Welcome to Python Programming"
print(greet_user("Ian"))
#Add Two Numbers
def add_numbers(num1, num2):
    return num1 + num2
print(add_numbers(4,12))
#Check if Even or Odd
def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
print(check_even_odd(4))
print(check_even_odd(22))
#Find the Largest Number
def find_largest(num1, num2, num3, num4):
    return max(num1, num2, num3, num4)
print(find_largest(4,12,22,23))
#Calculate Factorial
def calculate_factorial(n):
    factorial = 1
    for s in range(1, n + 1):
        factorial *= 1
        return factorial
    print(calculate_factorial)
#Reverse a String
def reverse_string(text):
    return text[::-1]
print(reverse_string("Python"))
#Numer in prime
def is_prime(number):
    if number < 2:
        return False
for s in range(2, int(number ** 0.5) +1):
    if number % s == 0:
        return False
    return True
print(is_prime(7))
print(is_prime(10))
