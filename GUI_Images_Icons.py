##################################################################
###   Author      : Doaa Maher              				  ####
###   File 		  : GUI Simple Images Display		  		  ####
###   Date        : 9 Dec 2020                	  		  	  ####
###   Version     : 1.0                   	      		      ####
##################################################################
from tkinter import *

root = Tk()

photo = PhotoImage(file="img.png")
label = Label(root, image = photo)
label.pack()

root.mainloop()