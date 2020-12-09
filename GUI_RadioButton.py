##################################################################
###   Author      : Doaa Maher              				  ####
###   File 		  : GUI Simple Radio Button			  		  ####
###   Date        : 9 Dec 2020                	  		  	  ####
###   Version     : 1.0                   	      		      ####
##################################################################
from tkinter import *

def Click_Submit():
	print("Done")

def Click_Male():
	print("Male Selected")
	
def Click_Female():
	print("Female Selected")

root=Tk()
frame= Frame(width = 500, height = 500)

radiobutton = Radiobutton(text="Male",value =1, command = Click_Male)
radiobutton2 = Radiobutton(text="Female",value = 2, command =Click_Female)

radiobutton.pack(expand = True, fill=X, side= TOP) 
radiobutton2.pack(expand = True, fill=Y, side= TOP)

button = Button(root, text="Enter", command=Click_Submit)
button.pack(expand= True, fill=X, side= RIGHT)

root.mainloop()