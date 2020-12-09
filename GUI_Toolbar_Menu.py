##############################################################
###   Author      : Doaa Maher              			  ####
###   File 		  : Updated : GUI Simple Toolbar Menu     ####
###   Date        : 9 Dec 2020                	  		  ####
###   Version     : 1.0                   	      		  ####
##############################################################
from tkinter import *

def Search_Word():
	word =input("Enter the Word you want to find : ")
	print("The word you're looking for is ",word)
	
def Search_Sentence():
	sentence =input("Enter the Sentence you want to find : ")
	print("The sentence you're looking for is ",sentence)

def New_Word():
	newword =input("Enter the New Word : ")
	print(newword, "Looks good! ")
	
def Settings_View():
	print("Cut , Copy, Paste, Open, Save, Save As...")

def Settings():
	setting =input("Enter the setting you want to change : ")
	print(setting, "Will be changed soon...")

root = Tk()
########################### TOOL BAR ###########################
toolbar = Frame(root, bg="blue")
toolbar.pack(side = LEFT, fill=X )

########################### MAIN MENU  ###########################
menu = Menu(root)
root.config(menu= menu)

subMenu = Menu(menu)
menu.add_cascade(label="Search" , menu = subMenu)
subMenu.add_command(label="Search for a word", command = Search_Word)
subMenu.add_command(label="Search for a sentence", command = Search_Sentence)
subMenu.add_command(label="New word...", command = New_Word)
subMenu.add_separator()
subMenu.add_command(label= "Exit",command = toolbar.quit)


SettingMenu = Menu(menu)
menu.add_cascade(label="Settings" , menu = SettingMenu)
SettingMenu.add_command(label="All Settings", command = Settings_View)
SettingMenu.add_command(label="Search for a setting...", command = Settings)
SettingMenu.add_separator()
SettingMenu.add_command(label= "Exit",command = toolbar.quit)

########################### TOOL BAR ###########################
Insertbutton = Button(toolbar, text = "New",bg= "red",fg="white")
Insertbutton.grid(row=0)

Insertbutton2 = Button(toolbar, text = "Open",bg="blue",fg="white" )
Insertbutton2.grid(row=0, column =1)

Insertbutton3 = Button(toolbar, text = "Exit",bg="black",fg="white",command = toolbar.quit )
Insertbutton3.grid(row=0, column =2)

root.mainloop()