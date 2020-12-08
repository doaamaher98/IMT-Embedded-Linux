##############################################################
###   Author      : Doaa Maher              			  ####
###   File 		  : Simple GUI Name & Password Entry	  ####
###   Date        : 8 Dec 2020                	  		  ####
###   Version     : 1.0                   	      		  ####
##############################################################
from tkinter import *
from tkinter.ttk import *

def Signin ():
	print("Welcome Back!")
	
def Signup ():
	print("Welcome new comer!")

root = Tk()

# Labels and Arranging them in rows and columns
list1= Label(root, text = "Name :").grid(row = 0, column = 0)
list2= Label(root, text = "Password :").grid(row = 1 , column = 0)

#Entry widget to take entry from the user and Arranging them in grid
entry1 = Entry(root).grid(row = 0, column = 1)
entry2 = Entry(root).grid(row = 1, column = 1)


# Checkbutton widget
check1 = Checkbutton(root, text="Remember me")
check1.grid(row = 2, column = 0, sticky = W , columnspan = 2)

# Button Widget and their grid
button3 = Button(root, text = "Sign in", command = Signin).grid(row= 2, column =4)
button4 = Button (root, text = "New? Sign up", command = Signup).grid(row=2, column =5)

mainloop()

