inventory = {
    "Mobile": 1,
    "Mouse": 2, 
    "CPU": 3,
    "Monitor": 4, 
    "Keyboard": 5, 
    "Laptop": 6, 
    "Speaker": 7, 
    "Mousepad": 8, 
    "ID Card": 9,
    "Graphics Card": 10,
    "Printer": 11, 
    "Scanner": 12, 
    "Vape": 13, 
    "Projector": 14, 
    "CCTV Camera": 15,
    
    }
def display(): 
    """Displays the items available in from dictionary"""
    print("\nAvailable Items:")
    for code, (name, price) in inventory.items():   #Loops through each item in inventory
        print (f"{code}: {name} - ${price:.2f}")    #Displays code, name and price of each item

display() #Calling the function
def select():
    code = input("*\nEnter code if item you want to buy: ").upper()
    if code in inventory: 
        return code
    else:
        print("Invalied code, try again")
        return None
    
#Calling 2 function and display item and price
display()

selected_code = None
while selected_code is None: # Will keep prompting until valid code is entered
    selected_code = select()

item_name, item_price = inventory(selected_code)
print(f"\nYou selected: {selected_code} - {item_name} (${item_price:.2f})")