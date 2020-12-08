######################################################
###   Author      : Doaa Maher              	  ####
###   File 		  : GUI Packing Buttons			  ####
###   Date        : 8 Dec 2020                	  ####
###   Version     : 1.0                   	      ####
######################################################

from tkinter import *

# Creating the window
root = Tk()

# Create a Frame that can expand acc to the size of window
panel = Frame(root)
panel.pack(fill = BOTH, expand = True)

# Button widget can also expand and fill
button1 = Button(panel, text = "Click me!", background = "red")
button1.pack (side = LEFT, fill = BOTH, expand = True)

# Button2 widget, doing the same expand and fill with a background and fg
button2 = Button(panel, text = "Click me too!", background = "blue", fg = "white")
button2.pack(side = LEFT, fill = BOTH, expand= True)

# Button3 widget, doing the same expand and fill with a background and fg
button2 = Button(panel, text = "Click me too!", background = "green")
button2.pack(side = LEFT, fill = BOTH, expand= True)

# Button4 widget, doing the same expand and fill with a background and fg
button2 = Button(panel, text = "Click me too!", background = "yellow")
button2.pack(side = LEFT, fill = BOTH, expand= True)


mainloop()