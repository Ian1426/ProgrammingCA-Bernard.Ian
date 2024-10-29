## Restaurant Order Discount (if-else)
print("A customer orders food at a restaurant")
total_bill = float(input("Enter the total bill:"))
if total_bill > 50:
    discount = total_bill * 0.1
    final_bill = total_bill - discount
    print(f"Discount applied! Your final bills is aed{final_bill}.")
else:
    print(f"No discount applied. Your total bill is aed{total_bill}")
## Movie Ticket Price (if-elif-else)
print("A cinema charges different ticket prices based on age")
age = float(input("Enter your age"))
if age <= 12: 
    print("Ticket price: 5 aed")
elif age <= 17:
    print("Ticket price: 7 aed")
elif age <= 64:
    print("The ticket price: 10 aed")
else:
    print("The ticket price: 6 aed")
  ## Bank Withdrwal (Nested if-else)
print("A customer withdraws money from bank account")  
amount = int(input("Enter the account balance: "))
amount = int(input("Enter the amount to withdraw: "))
if amount <= 1000: 
   if amount == 1000:
       print("")



