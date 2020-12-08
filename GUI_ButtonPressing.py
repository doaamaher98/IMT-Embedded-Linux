######################################################
###   Author      : Doaa Maher              	  ####
###   File 		  : GUI Button Pressing tracking  ####
###   Date        : 8 Dec 2020                	  ####
###   Version     : 1.0                   	      ####
######################################################
from tkinter import *

root = Tk ()
root.title("Welcome to Tkinter")
root.geometry('400x100')

# A function to track the button pressings
def ButtonFunction () :
	print("Button is Pressed!")

button = Button(root, text="Click me!", bd = "5", command = ButtonFunction)
button.pack(side = "top")


root.mainloop()
