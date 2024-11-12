number = int(input("Enter a number: "))
while number >= 0:
    print(number)
    number -= 1
##
n = -2
while n < 5: 
    print(f'Inside the loop, the value of n is (n).')
    n += 5 #Increment is +
           #Decrement is - 
##
total = 0
for s in range(8,1):
    total += 1
print("Sum:", total)
##
word = input("Enter a string: ")
for char in word:
    print(char)
