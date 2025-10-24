#!C:\Users\ian\AppData\Local\Programs\Python\Python312\python.exe

#mtg_card_csv_import
#Program to perform some search functions on the CSV master file exported from my PHP page, "process_card.php"
from functools import partial
import csv
from hashlib import new
import re
import pprint
import tkinter as tk
from tkinter import ttk


def create_popup(Color):
    # Create a popup window and populate with a Frame object
    output_window=tk.Tk()
    output_window.title(f"{Color} cards")
    output_window.geometry('1200x800')
    return output_window
    
def create_frame(output_window):
    frame=tk.Frame(output_window)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    return frame

def create_scrollbar(frame):
    # create a scrollbar and add it to the frame
    v_scrollbar=tk.Scrollbar(frame)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    return v_scrollbar
    
# Print all cards with a specific color
def listCardsByColor(list, Color):
    # Create a popup window and populate with a Frame object
    
    #Call create_popup function to obtain a window
    output_window = create_popup(Color)
    #Call create_frame function to obtain a Frame
    frame=create_frame(output_window)
    #Call create_scrollbar to obtain a scrollbar
    v_scrollbar=create_scrollbar(frame)
    
    #Iterate over list and append rows that contain the Color
    count=0
    outlist=[]
    for row in list:
        if Color in row:
            add_this=str(row).strip("[")
            #print (add_this) #debugging
            outlist.append("\n"+add_this)
            count+=1
    output_window.title(f"{Color} cards, Total Count: {count}")
    
    # create a text widget and add it to the frame
    if Color=="Colorless":
        backgrdclr="Grey"
        txt_clr="white"
    elif Color=="Multi-Color":
        backgrdclr="purple"
    else: backgrdclr=Color
    if backgrdclr=="Black" or backgrdclr=="Grey":
        txt_clr="white"
    else: txt_clr="black"
    text=tk.Text(frame, height=8, fg=txt_clr, bg=backgrdclr)
    text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    
    # configure scrollbar
    text['yscrollcommand']=v_scrollbar.set
    v_scrollbar.config(command=text.yview)
    
    # insert output text into the text widget
    for row in outlist:
        #print (row) #debugging
        clean_row=row.strip("]")
        #print (clean_row) #debugging
        text.insert(tk.END,str(clean_row +"\n"))
    

#Print all rows from the CSV file

def printAllCards(list):
    
    #Call create_popup function to obtain a window
    output_window = create_popup("All")
    #Call create_frame function to obtain a Frame
    frame=create_frame(output_window)
    #Call create_scrollbar to obtain a scrollbar
    v_scrollbar=create_scrollbar(frame)
    count=0
    outlist=[]
    for row in list:
        add_this=str(row).strip("[")
        #print (add_this) #debugging
        outlist.append("\n"+add_this)
        count+=1
    output_window.title(f"All cards, Total Count: {count}")
    
    # create a text widget and add it to the frame
    text=tk.Text(frame, height=8)
    text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    
    # configure scrollbar
    text['yscrollcommand']=v_scrollbar.set
    v_scrollbar.config(command=text.yview)
    
    # insert output text into the text widget
    for row in outlist:
        #print (row) #debugging
        clean_row=row.strip("]")
        #print (clean_row) #debugging
        text.insert(tk.END,str(clean_row +"\n"))

#Print all cards of a specific type
def printCardsbyType(list, spellType):
    #Call create_popup function to obtain a window
    output_window = create_popup("All")
    #Call create_frame function to obtain a Frame
    frame=create_frame(output_window)
    #Call create_scrollbar to obtain a scrollbar
    v_scrollbar=create_scrollbar(frame)
    count=0
    outlist=[]
    for row in list:
        if spellType in row:
            add_this=str(row).strip("[")
            #print (add_this) #debugging
            outlist.append("\n"+add_this)
            count+=1
    output_window.title(f"{spellType} cards, Total Count: {count}")
    
    # create a text widget and add it to the frame
    text=tk.Text(frame, height=8)
    text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    
    # configure scrollbar
    text['yscrollcommand']=v_scrollbar.set
    v_scrollbar.config(command=text.yview)
    
    # insert output text into the text widget
    for row in outlist:
        #print (row) #debugging
        clean_row=row.strip("]")
        #print (clean_row) #debugging
        text.insert(tk.END,str(clean_row +"\n"))

#Print all cards of a specific rarity
def printByRarity(list,rarity):
    #Call create_popup function to obtain a window
    output_window = create_popup("Rarity")
    #Call create_frame function to obtain a Frame
    frame=create_frame(output_window)
    #Call create_scrollbar to obtain a scrollbar
    v_scrollbar=create_scrollbar(frame)
    count=0
    outlist=[]
    for row in list:
        if rarity in row:
            add_this=str(row).strip("[")
            #print (add_this) #debugging
            outlist.append("\n"+add_this)
            count+=1
    output_window.title(f"{rarity} cards, Total Count: {count}")
    
    # create a text widget and add it to the frame
    text=tk.Text(frame, height=8)
    text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    
    # configure scrollbar
    text['yscrollcommand']=v_scrollbar.set
    v_scrollbar.config(command=text.yview)
# insert output text into the text widget
    for row in outlist:
        #print (row) #debugging
        clean_row=row.strip("]")
        #print (clean_row) #debugging
        text.insert(tk.END,str(clean_row +"\n"))
        
#Search by Card Name
def printBySearchName(aList):
    #print(searchStr) #debugging
    #Call create_popup function to obtain a window
    search_window=tk.Tk()
    search_window.title("Search for a card")
    search_window.geometry('300x150')
    label = tk.Label(search_window)
    label.config(text='Enter a string to search for')
    txt = tk.Entry(search_window, width=20)
    txt.focus()
    searchStr=txt.get()
    #print(txt) #debugging
    record_input_callable=partial(record_search_input, txt,aList)
    btn = tk.Button(search_window, text="Submit", command=record_input_callable)
    label.grid(row=0, column=0)
    txt.grid(row=1, column=0)
    btn.grid(row=1, column=1)
    search_window.mainloop()
    
def output_card_search(searchStr,aList):  
    #Call create_popup function to obtain a window
    #print (searchStr) #debugging
    output_window = create_popup("Searched ")
    #Call create_frame function to obtain a Frame
    frame=create_frame(output_window)
    #Call create_scrollbar to obtain a scrollbar
    v_scrollbar=create_scrollbar(frame)
    count=0
    outlist=[]
    if isinstance(searchStr,str): 
        try:
            list = [card for card in aList if searchStr.lower() in card[0].lower()]
            for row in list:
                #print (row) #debugging
                add_this=str(row).strip("[")
                outlist.append("\n"+add_this)
                count+=1
            if count==0:
                outlist.append("Card not found")
            
        except Exception as e:
            print("Invalid Entry)")
    output_window.title(f"{searchStr} cards, Total Count: {count}")        
    # create a text widget and add it to the frame
    text=tk.Text(frame, height=8)
    text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    
    # configure scrollbar
    text['yscrollcommand']=v_scrollbar.set
    v_scrollbar.config(command=text.yview)
# insert output text into the text widget
    for row in outlist:
        #print (row) #debugging
        clean_row=row.strip("]")
        #print (clean_row) #debugging
        text.insert(tk.END,str(clean_row +"\n"))
   
#Search by Set Name
def printBySetName(aList):
    
    #print(searchStr) #debugging
    #Call create_popup function to obtain a window
    search_window=tk.Tk()
    search_window.title("Search for a set name")
    search_window.geometry('300x150')
    label = tk.Label(search_window)
    label.config(text='Enter a string to search for')
    txt = tk.Entry(search_window, width=20)
    txt.focus()
    setName=txt.get()
    #print(txt)
    record_input_callable=partial(record_setsearch_input,txt,aList)
    btn = tk.Button(search_window, text="Submit", command=record_input_callable)
    label.grid(row=0, column=0)
    txt.grid(row=1, column=0)
    btn.grid(row=1, column=1)
    search_window.mainloop()
    
def output_set_search(setName,aList):
    #Call create_popup function to obtain a window
    #print (searchStr) #debugging
    output_window = create_popup("Searched ")
    #Call create_frame function to obtain a Frame
    frame=create_frame(output_window)
    #Call create_scrollbar to obtain a scrollbar
    v_scrollbar=create_scrollbar(frame)
    count=0
    outlist=[]
    if isinstance(setName,str):
        try:
            list = [set_n for set_n in aList if setName.lower() in set_n[4].lower()]
            for row in list:
                    #print (row) #debugging
                    add_this=str(row).strip("[")
                    outlist.append("\n"+add_this)
                    count+=1
            if count==0:
                outlist.append("Set not found")
        except Exception as e:
            print("Invalid Entry)")
    output_window.title(f"{setName} cards, Total Count: {count}") 
 # create a text widget and add it to the frame
    text=tk.Text(frame, height=8)
    text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    
    # configure scrollbar
    text['yscrollcommand']=v_scrollbar.set
    v_scrollbar.config(command=text.yview)
# insert output text into the text widget
    for row in outlist:
        #print (row) #debugging
        clean_row=row.strip("]")
        #print (clean_row) #debugging
        text.insert(tk.END,str(clean_row +"\n"))


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

#Callback function for when the Submit button is pressed. Passes user's menu choice when calling the main function
def record_input(txt):
    choice=txt.get()
    main(choice)
    
def record_search_input(txt,aList):
    searchStr=txt.get()
    output_card_search(searchStr,aList)
    
def record_setsearch_input(txt,aList):
    setName=txt.get()
    output_set_search(setName,aList)

#Create the menu popup window and get the user's input from the box
def show_menu():
    root=tk.Tk()
    root.title("Magic CSV Search")
    root.geometry('400x400')
    label = tk.Label(root)
    label.config(text='0-Show Red cards\n 1-Show Green Cards\n 2-Show Blue cards\n 3-Show Black cards\n 4-Show White cards\n 5-Show Mult-Color cards\n 6-Show Colorless Cards\n 7-Show All Sorceries\n 8-Show all Creatures\n 9-Show all Instants\n A-Show All Lands\n B-Show All Enchantments\n C-Show All Artifacts\n D-Show All Commons\n E-Show all Uncommons\n F-Show All Rares\n 11-Show All Mythic Rares\n 12-Search by Card Name\n 13-Show Cards by Set\n FF-Show all cards\n Q-Quit" \n Enter a menu choice:')
    txt = tk.Entry(root, width=2)
    txt.focus()
    choice=txt.get()
    record_input_callable=partial(record_input, txt)
    btn = tk.Button(root, text="Submit", command=record_input_callable)
    label.grid(row=0, column=0)
    txt.grid(row=1, column=0)
    btn.grid(row=1, column=1)
    root.mainloop()
    
    
#The main function of the program
def main(choice):
    choice=choice.lower()
    match choice:
        case "0":
            listCardsByColor(myList,"Red")

        case "1":
            listCardsByColor(myList,"Green")

        case "2":
            listCardsByColor(myList,"Blue")

        case "3":
            listCardsByColor(myList,"Black")

        case "4":
            listCardsByColor(myList,"White")

        case "5":
            listCardsByColor(myList,"Multi-Color")

        case "6":
            listCardsByColor(myList,"Colorless")
        
        case "7":
            printCardsbyType(myList,"Sorcery")

        case "8":
            printCardsbyType(myList,"Creature")
        
        case "9":
            printCardsbyType(myList,"Instant")

        case "a":
            printCardsbyType(myList,"Land")

        case "b":
            printCardsbyType(myList,"Enchantment")

        case "c":
            printCardsbyType(myList,"Artifact")

        case "d":
            printByRarity(myList,"Common")

        case "e":
            printByRarity(myList,"Uncommon")

        case "f":
            printByRarity(myList,"Rare")

        case "11":
            printByRarity(myList,"Mythic Rare")

        case "12":
            printBySearchName(myList)

        case "13":
            printBySetName(myList)

        case "ff":
            printAllCards(myList)
        
        case "q":
            exit()
        
        case _:
            print("That isn't an option.")

#program starting point. User enters the CSV filename they want to parse into the app. Then start the menu function.        
fileName=input("Enter the CSV file name to parse:")
myList=import_CSV_to_List(fileName.strip('\"'))

show_menu()

