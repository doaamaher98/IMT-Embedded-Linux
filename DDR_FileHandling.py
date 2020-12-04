##########################################################
###   Author      : Doaa Maher               		  ####
###   File 		  : Generating Init function for DDRA ####
###					In ATMEGA32 uC			  		  ####
###   Date        : 4 Dec 2020                		  ####
###   Version     : 1.0                               ####
##########################################################
file = open("Init.c","a")
file.write("void Init_PORTA_Direction (void)")
file.write("\n{")
file.write("\n	DDRA = 0b")

i = 0
while i <= 7 :
	print("Please enter Bit",i,"mode : ")
	mode = input()
	if mode == "input" :
		file.write("0")
		i+=1
		
	elif mode == "output" :
		file.write ("1")
		i+=1
		
	else :
		print("Wrong input, Please try again")

file.write("\n}")
file.close()