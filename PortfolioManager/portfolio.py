import os
import fileinput
import json


filename = "PortfolioManager/data/portfolio.json"

def menuDisplay():
    print('=============================')
    print('= Portfolio Management Menu =')
    print('=============================')
    print('(1) Buy New Stock to Inventory')
    print('(2) Sell Stock from Inventory')
    print('(3) Update Inventory')
    print('(4) Search Item in Inventory')
    print('(5) Print Inventory Report')
    print('(99) Quit')
    CHOICE = int(input("Enter choice: "))
    menuSelection(CHOICE)

def menuSelection(CHOICE):
    if CHOICE == 1:
        addInventory()
    elif CHOICE == 2:
        removeInventory()
    elif CHOICE == 3:
        updateInventory()
    elif CHOICE == 4:
        searchInventory()
    elif CHOICE == 5:
        printInventory()
    elif CHOICE == 7:
        view_data()
    elif CHOICE == 99:
        exit()

def view_data():
    with open(filename, "r") as f:
        temp = json.load(f)
        for entry in temp:
            symbol = entry['symbol']
            price = entry['price']
            print(f"{symbol} price is {price}")

        


def addInventory():
    item_data = {}
    with open (filename, "r") as f:
        temp = json.load(f)
    item_data["symbol"] = input("Symbol: ")
    item_data["price"] = float(input("Price: "))
    item_data["amount"] = float(input("Amount: "))
    temp.append(item_data)
    with open (filename, "w") as f:
        json.dump(temp, f, indent=4)

    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
    
def removeInventory():
    print("Removing Inventory")
    print("==================")
    e.strip('\n'), end='\n')
    item_description
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def updateInventory():
    print("Updating Inventory")
    print("==================")
    view_data()
    new_data = []
    with open (filename, "r") as f:
        temp = json.load(f)
        data_length = len(temp)-1
    print("Which index number would you like to update")
    edit_option = input(f"Select a number 0-{data_length}")
    i=0
    for entry in temp:
        if i == int(edit_option):
            symbol = entry["symbol"]
            price = entry["price"]
            

    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def searchInventory():
    print('Searching Inventory')
    print('===================')
    item_description = input('Enter the name of the item: ')
    
    f = open('Inventory.txt', 'r')
    search = f.readlines()
    f.close
    for i, line in enumerate(search):
        if item_description in line:
            for b in search[i:i+1]:
                print('Item:     ', b, end='')
            for c in search[i+1:i+2]:
                print('Quantity: ', c, end='')
                print('----------')
        
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
        
def printInventory():
    InventoryFile = open('Inventory.txt', 'r')
    item_description = InventoryFile.readline()
    print('Current Inventory')
    print('-----------------')
    while item_description != '':
        item_quantity = InventoryFile.readline()
        item_description = item_description.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        print('Item:     ', item_description)
        print('Quantity: ', item_quantity)
        print('----------')
        item_description = InventoryFile.readline()
    InventoryFile.close()

    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

menuDisplay()
