######################################################
###   Author      : Doaa Maher                    ####
###   File 		    : GUI Button Image			        ####
###   Date        : 8 Dec 2020                	  ####
###   Version     : 1.0                   	      ####
######################################################
from tkinter import *

# Tkinter window creation
root = Tk()

# Adding the widgets and packing it on top
Label(root, text = "ImageButton", font = ("Arial", 20)).pack(side = TOP)

# Creating PhotoImage object to use image
photo = PhotoImage(file = "img.png") 

# Return a new Photoimage based on the same image 
# Subsample to scale the photo
photo = photo.subsample(1,1)

# Set image to overwrite the button and pack it on top
Button(root , text = "" , image = photo).pack(side = TOP)

mainloop()
