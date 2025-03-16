#mtg_card_csv_import
#Program to perform some functions on the CSV master file exported from my PHP page, "C:\Users\ian\OneDrive\Magic Card Inventory webpage\process_card.php"

import csv
from hashlib import new
import re
import pprint

#Decorator function to print lists
def print_some_hashes (func):
    def wrapper(*args, **kwargs):
        count=func(*args, **kwargs)
        print("#"*40)
        print(f"Total Cards:{count}")
    return wrapper

# Print all cards with a specific color
@print_some_hashes
def listCardsByColor(list, Color):
    count=0
    for row in list:
        if Color in row:
            pprint.pp(row, width=40)
            count+=1
    return count

#Print all rows from the CSV file
@print_some_hashes
def printAllCards(list):
    count=0
    for row in list:
        pprint.pp(row, width=40)
        count+=1
    return count

#Print all cards of a specific type
@print_some_hashes
def printCardsbyType(list, spellType):
    count=0
    for row in list:
        if spellType in row:
            pprint.pp(row, width=40)
            count+=1
    return count

#Print all cards of a specific rarity
@print_some_hashes
def printByRarity(list,rarity):
    count=0
    for row in list:
        if rarity in row:
            pprint.pp(row, width=40)
            count+=1
    return count

#Search by Card Name
@print_some_hashes
def printBySearchName(searchStr,aList):
    print(searchStr)
    if isinstance(searchStr,str): 
        try:
            newlist = [card for card in aList if searchStr.lower() in card[0].lower()]
            pprint.pp(newlist, width=40)
            count=newlist.__len__()
            if count==0:
                print("Card not found")
            return count 
        except Exception as e:
            print("Invalid Entry)")
    input("\nPress Enter to continue...")
   
#Search by Set Name
@print_some_hashes
def printBySetName(setName,aList):
    count=0
    if isinstance(setName,str):
        try:
            setlist = [set_n for set_n in aList if setName.lower() in set_n[4].lower()]
            pprint.pp(setlist, width=40)
            count=setlist.__len__()
            print(f"Total matches: {count}")
            if count==0:
                print("Set name not found")
            return count
        except Exception as e:
            print("Invalid Entry)")
        input("\nPress Enter to continue...")

#Import CSV file specified by user into a list
def import_CSV_to_List(file):
   try:
    with open(file,mode='r') as f:
        csv_reader=csv.reader(f,delimiter="\t")
        aList=[]
        for row in csv_reader:
            aList.append(row)
        return aList
   except Exception as e:
        print("Error loading CSV file")
        print(e)
        input("\nPress Enter to continue...")

fileName=input("Enter the CSV file name to parse:")
myList=import_CSV_to_List(fileName.strip('\"'))

while True:
    print(" 0-Show Red cards\n 1-Show Green Cards\n 2-Show Blue cards\n 3-Show Black cards\n 4-Show White cards\n 5-Show Mult-Color cards\n 6-Show Colorless Cards\n 7-Show All Sorceries\n 8-Show all Creatures\n 9-Show all Instants\n A-Show All Lands\n B-Show All Enchantments\n C-Show All Artifacts\n D-Show All Commons\n E-Show all Uncommons\n F-Show All Rares\n 11-Show All Mythic Rares\n 12-Search by Card Name\n 13-Show Cards by Set\n FF-Show all cards\n Q-Quit")
    choice=input("Enter a menu choice:")
    choice=choice.lower()
    match choice:
        case "0":
            print_some_hashes(listCardsByColor(myList,"Red"))
            input("\nPress Enter to continue...")

        case "1":
            listCardsByColor(myList,"Green")
            input("\nPress Enter to continue...")

        case "2":
            listCardsByColor(myList,"Blue")
            input("\nPress Enter to continue...")

        case "3":
            listCardsByColor(myList,"Black")
            input("\nPress Enter to continue...")

        case "4":
            listCardsByColor(myList,"White")
            input("\nPress Enter to continue...")

        case "5":
            listCardsByColor(myList,"Multi-Color")
            input("\nPress Enter to continue...")

        case "6":
            listCardsByColor(myList,"Colorless")
            input("\nPress Enter to continue...")
        
        case "7":
            printCardsbyType(myList,"Sorcery")
            input("\nPress Enter to continue...")

        case "8":
            printCardsbyType(myList,"Creature")
            input("\nPress Enter to continue...")
        
        case "9":
            printCardsbyType(myList,"Instant")
            input("\nPress Enter to continue...")

        case "a":
            printCardsbyType(myList,"Land")
            input("\nPress Enter to continue...")

        case "b":
            printCardsbyType(myList,"Enchantment")
            input("\nPress Enter to continue...")

        case "c":
            printCardsbyType(myList,"Artifact")
            input("\nPress Enter to continue...")

        case "d":
            printByRarity(myList,"Common")
            input("\nPress Enter to continue...")

        case "e":
            printByRarity(myList,"Uncommon")
            input("\nPress Enter to continue...")

        case "f":
            printByRarity(myList,"Rare")
            input("\nPress Enter to continue...")

        case "11":
            printByRarity(myList,"Mythic Rare")
            input("\nPress Enter to continue...")

        case "12":
            searchCard=input("Search by card name:")
            printBySearchName(searchCard,myList)
            input("\nPress Enter to continue...")

        case "13":
            setName=input("Search by set name:")
            printBySetName(setName,myList)
            input("\nPress Enter to continue...")

        case "ff":
            printAllCards(myList)
            input("\nPress Enter to continue...")
        
        case "q":
            exit()
        
        case _:
            print("That isn't an option.")
