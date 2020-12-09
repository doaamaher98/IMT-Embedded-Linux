##################################################################
###   Author      : Doaa Maher              				  ####
###   File 		  : GUI Simple Message Box Example	  		  ####
###   Date        : 9 Dec 2020                	  		  	  ####
###   Version     : 1.0                   	      		      ####
##################################################################

from tkinter import *
import tkinter.messagebox

root = Tk()

#### The Simple/Basic message box
# tkinter.messagebox.showinfo("Window title", "This is the displayed message!")

#### Message box with [YES,NO] options in a Question
answer = tkinter.messagebox.askquestion("Question 1", "Are you new to the website?")
if answer == 'yes' :
	print("Welcome, you'll enjoy it!")
else :
		print("Welcome back!")

root.mainloop()