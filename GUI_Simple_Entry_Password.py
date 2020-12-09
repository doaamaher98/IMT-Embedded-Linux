##############################################################
###   Author      : Doaa Maher              			  ####
###   File 		  : Simple GUI Name & Password Entry	  ####
###   Date        : 8 Dec 2020                	  		  ####
###   Version     : 1.0                   	      		  ####
##############################################################
def PrintWelcome ():
	print("Welcome back!")
		
def PrintSignUp ():
	print ("You'll enjoy it!")
	
		
root = Tk()
frame = Frame(root, width = 500, height = 1000)


Name = Label(root, text="Name : ").grid(row = 0, sticky= E)
Password = Label (root, text = "Password : ").grid(row=1, sticky= E)

entry1 = Entry(root).grid(row=0, column=1)
entry2 = Entry(root).grid(row=1, column=1)

button1 = Button (root, text = "Sign in",command= PrintWelcome ).grid(columnspan =2)
button2 = Button (root, text = "Sign up",command = PrintSignUp).grid(row=3, column=2)
buttonExit = Button (root, text = "Exit",command =frame.quit ).grid (row=3, column = 3)


root.mainloop()

