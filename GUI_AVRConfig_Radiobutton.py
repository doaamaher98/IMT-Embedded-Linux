##################################################################
###   Author      : Doaa Maher              				  ####
###   File 		  : GUI AVR Config with Radio Button		  ####
###   Date        : 9 Dec 2020                	  		  	  ####
###   Version     : 1.0                   	      		      ####
##################################################################
import tkinter

labels        = list()
Radio_Inputs  = list()
Radio_Outputs = list()
Radio_Vars    = list()

def Init_root():
	#Create Main Window
	global root
	root = tkinter.Tk()
	root.geometry("320x380+100+100")
	root.resizable(width = False, height = False)
	root.title("AVR Configuration")
	
	i=0
	while i< 4:
		root.columnconfigure(i,minsize='10m')
		i+=1
	i=0
	while i<10:
		root.rowconfigure(i,minsize='10m')
		i+=1
		
def Create_labels():
	i =0
	while i < 8:
		labels.append( tkinter.Label(root,text = "Pin "+str(i)+" Mode") )
		labels[i].grid(row = i, column = 0)
		i+=1
		
def Create_Radio():
	i=0
	while i< 8:
		Radio_Vars.append( tkinter.IntVar() )
		Radio_Inputs.append( tkinter.Radiobutton(root, text= "Input", 
												 variable = Radio_Vars[i],
												 value    = 0)  )
		Radio_Outputs.append( tkinter.Radiobutton(root, text= "Ouput", 
												  variable = Radio_Vars[i],
												  value    = 1)  )
		Radio_Inputs[i].grid(row=i,column=2)
		Radio_Outputs[i].grid(row=i,column=3)
		i+=1
		
def Create_Button():
	Generate = tkinter.Button(root,text="Generate", command=generate)
	Generate.grid(row=9,column=3)
	
def generate():
	i    = 0
	DDRA = ""
	while i < 8:
		value = Radio_Vars[i].get()
		DDRA  = str(value) + DDRA
		i += 1
		
	DDRA = "0b" + DDRA
	f = open("config.c","w")
	f.write("void DDRA_Config (void)\n")
	f.write("{\n")
	f.write("	DDRA = "+str(DDRA)+" ;\n")
	f.write("}\n")
	f.close()
	
Init_root()
Create_labels()
Create_Radio()
Create_Button()

root.mainloop()