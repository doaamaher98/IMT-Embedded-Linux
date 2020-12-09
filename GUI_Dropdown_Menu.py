##############################################################
###   Author      : Doaa Maher              			  ####
###   File 		  : GUI Simple Dropdown Menu	  		  ####
###   Date        : 9 Dec 2020                	  		  ####
###   Version     : 1.0                   	      		  ####
##############################################################
from tkinter import *

# Functions to serve the Commands in the dropdown menu
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

# Main window
root = Tk()
# Frame
frame = Frame(width = 500, height = 600)
# Creating the Menu object
menu = Menu(root)
root.config(menu= menu)

# Creating the subMenu
subMenu = Menu(menu)
# Get the dropdown menu :
menu.add_cascade(label="Search" , menu = subMenu)
subMenu.add_command(label="Search for a word", command = Search_Word)
subMenu.add_command(label="Search for a sentence", command = Search_Sentence)
subMenu.add_command(label="New word...", command = New_Word)
subMenu.add_separator()
subMenu.add_command(label= "Exit",command = frame.quit)

# Creating another subMenu
SettingMenu = Menu(menu)
menu.add_cascade(label="Settings" , menu = SettingMenu)
SettingMenu.add_command(label="All Settings", command = Settings_View)
SettingMenu.add_command(label="Search for a setting...", command = Settings)
SettingMenu.add_separator()
SettingMenu.add_command(label= "Exit",command = frame.quit)

root.mainloop()