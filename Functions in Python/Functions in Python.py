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
#Passing Arguments to Functions
def main ():
    value = 5
    show_double(value)

    def show_double(number):
        result = number * 2
        print(result)
#Counting the numbers to volwers in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0 
    for char in text:
        if char in vowels:
            count += 1
    return count
print(count_vowels("I love python programming."))
#Find the Maximum in a List
def find_max_in_list(numbers):
    return max(numbers)
print(find_max_in_list([1, 4, 12, 16, 22]))