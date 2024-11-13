#Sample 
num = int(input("Enter a number: "))
for s in range(1, 11):
    print(f"{num} x {s} = {num * s} ")
#Find prime numbers 
for s in range(0,51):
    if s % 2 != 0:
        print(s)
#Find Minimum in a List
numbers = [12, 4, 56, 17, 8]
minimum = numbers[0]
for num in numbers: 
    if num < minimum:
        minimum = num
print("Minimum value:", minimum)
#Guess the Number Game
import random
target = random.randint(1, 50)
guess = None
while guess != target:
    guess = int(input("Guess a number between 1 and 50: "))
    if guess < target: 
        print("Too Low")
    elif guess > target:
        print("Too high")
print("Correct! You guessed the number.")