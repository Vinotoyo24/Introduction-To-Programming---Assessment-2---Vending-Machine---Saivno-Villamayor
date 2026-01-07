from datetime import datetime

"""

Vending Machine : Assessment 2 : Savino Villamayor

This Program demonstrates knowledge of programming and
techniques gathered over the course of the module in 
developing a python program language to simulate a 
console-based Vending Machine.

"""

 # Utilized A Dictionary for Storing The Vending Machine Items
 # This Stores Each Item Product/Brand, Price, and Available Stock
items = {"A1" : {"PRD" : "Coke", "Price" : 5.25, "Stock" : 1},
         "A2" : {"PRD" : "Pepsi", "Price" : 5, "Stock" : 5},
         "A3" : {"PRD" : "Fanta", "Price" : 5.25, "Stock" : 5},
         "B1" : {"PRD" : "Pringles", "Price" : 4, "Stock" : 5},
         "B2" : {"PRD" : "Cheetos", "Price" : 3, "Stock" : 5}}

 # Starting Point of the The System Using A Function
def Start():
    while True:
        dec = input("Press O to Order : ").title() 
        if dec == 'O':
            OrVendingMachine() # Start Ordering Process
        elif dec == 'A':
            Admin() # Admin Controls
        else:
            print("Error")
    
 # Handles the Vending Machine Process
def OrVendingMachine():
    
    print("\n")
    global Money # Global Variable for Storing Inserted Balance
    Display() # Display Vending Machine Menu
    
     # This Loop Ensures Valid Money Input
    while True:
        amount = input("Enter Amount of Money: ")
        try:
            Money = float(amount)
            break
        except ValueError:
            print("Try Again!")
    
     # This While Do Loop Ensurese A Valid Product is Selected
    while True:
        selection = str(input("Enter Product Index : ")).title()
        if selection in items:
            Order(selection)
            break
        else:
            print("Invalid Entered Index!\n")
            continue

 # This Function Displays the Vending Machine Menu/Items
def Display():
    
    print("********VENDING MACHINE********")
    print("*******************************")
    
    # Loops All Through Products and Displays Details
    for key, value in items.items():
        print(f"{key} : {value['PRD']} - ${value["Price"]} - Stock - {value["Stock"]}")

    print("*******************************")
    
    
     # Time-Based Recommendation System
    time = datetime.now().hour
    
    if 6 <= time < 10:
        print(">>> Good Morning ! 😊\nWould Recommend Energy Drinks or Coffee to Keep You Going for The Rest of the Day!\n")
    elif 10 <= time < 18:
        print(">>> Its Afternoon Now ! 😍\nTry Some Snacks !\n")
    else:
        print(">>> Its Evening Now ! 🥱\nWould Recommend Something Light !\n")

 # This Function Handles the Ordering Process
def Order(selection):
    print("\n")
    global Money
    product = items[selection]
    
    Money = float(Money)
    
     # Checks if Products/Items is in Stock
    if product["Stock"] <= 0:
        print(f"Insufficient Stock! \nSorry! {product["PRD"]} is unfortunately out of Stock 😥")
        return
    
     # Checks if Balance is Sufficient
    if Money < product["Price"]:
        print("Insufficient Funds!")
        return
    
    product["Stock"] -= 1 # Updates the Stock
    Receipt(product, Money)

 # Dispenses Product and Generates a Receipt
def Receipt(product, Money):
    currenttime = datetime.now().strftime("%H:%M:%S")
    
    print("*******************\n      RECEIPT      \n*******************")
    print("Decription :  Price")
    print(f"1x {product["PRD"]}   :   ${product["Price"]}")
    print("*******************")
    print(f"Total    :   ${product["Price"]}")
    print(f"Money    :    {Money}")
    print(f"Change    :    {Money - product["Price"]}")
    print(f"< Ordered at : [{currenttime}] >\n")


##############################################################################

 # Admin Menu for Managing Vending Machine Items
def Admin():
    print("\n~~~ ADD/REMOVE PRODUCTS ~~~")
    i = input("<Admin> Do you Want to Add/Remove Product(s)? (A/R) : ").title()
    if i == "A":
        Display()
        AddProducts()
    elif i == "R":
        Display()
        RemoveProducts()
    else:
        Start()

 # Removes Products From The Vending Machine
def RemoveProducts():
    print("~~~ REMOVING PRODUCTS ~~~")
    
    while True:
        rmv = input("Which Index Number Do you Want to Remove? : ").title()
        if rmv in items:
            items.pop(rmv)
            print("Successfully Removed {rmv} !")
            break
        else:
            print("Invalid index !")  

 # Adds or Replaces Products from the Vending Machine
def AddProducts():
    print("~~~ ADD/REPLACE PRODUCTS ~~~")
    
    while True:
        a = input("Enter New Index Number : ").title()
        if len(a) == 2 and a[0].isalpha() and a[1].isnumeric():
            a.capitalize()
            break
        else:
            print("Enter Valid Index (e.g, A2, B5, C2) !")
        
    pt = input("Enter Product Brand/Name : ")
    
    while True:
        try:
            pr = float(input(f"Enter {pt} Price : "))
            break
        except ValueError:
            print("invalid Price !")
            
    while True:
        sk = input(f"Enter {pt} ${pr} Stocks : ")
        if sk.isnumeric():
            sk = int(sk)
            break
        else:
            print("Invalid Stock !")
            
     # Add or Replaces Product to The Items Dictionary
    items[a] = {"PRD" : pt, "Price" : pr, "Stock" : sk}
    
    product = items[a]
    
    print(f"Added New Product : {product["PRD"]} ${pr}\n")

 # Inilization of The Code <<<
print("~~~ Vending Machine ~~~ \nEnter O to Order, or Enter A \nto Access Admin Controls\n")
Start()

