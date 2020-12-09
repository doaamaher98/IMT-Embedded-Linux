##############################################################
###   Author      : Doaa Maher              			  ####
###   File 		  : GUI Name & Password Entry	  		  ####
###   Date        : 9 Dec 2020                	  		  ####
###   Version     : 1.0                   	      		  ####
##############################################################
from tkinter import *

def EnterData():
	User = User_Entry.get()
	Pass = Pass_Entry.get()
	print("Welcome!",User)

# Create Main Window
root = Tk()
frame= Frame(width = 500, height = 1000)


i=0
while i<4:
	root.columnconfigure(i,minsize='10')
	i+=1
i=0
while i<4:
	root.rowconfigure(i,minsize='10')
	i+=1

# Create Data Entry Label
user_Name = Label(root, text = "Name").grid(row = 0, column = 0,sticky=E) 
user_password = Label(root, text = "Password").grid(row = 1, column = 0,sticky=E)

# Create Entry
User_Entry = Entry(root)
Pass_Entry = Entry(root, show = '*')
User_Entry.grid(row = 0, column = 1)
Pass_Entry.grid(row = 1, column = 1)

# Create Button to Sign in
Sign_Button = Button(root,text= "Sign in",background= "black", fg="white", command = EnterData).grid(row = 3, column = 2)

# Create Button to Exit
Exit_Button = Button(root, text="Exit",background= "blue", fg="white", command = frame.quit).grid(row = 4, column = 2,sticky=E)

root.mainloop()