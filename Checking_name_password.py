########################################################
###   Author      : Doaa Maher                		####
###   File 		  : Checking name and passwords     ####
###   Date        : 4 Dec 2020                		####
###   Version     : 1.0                       		####
########################################################



Name = str(input("Please enter your name : "))
if Name == 'Ahmed' or Name == 'Ali' or Name == 'Amr' or Name == 'Doaa':
	Pass = int(input("Please enter your Password : "))
	if Pass == 1234 :
		print("Welcome back Ahmed!")
	elif Pass == 6078 :
		print("Welcome back Ali!")
	elif Pass == 9345 :
		print("Welcome back Amr!")
	elif Pass == 1998 :
		print("Welcome back Doaa!")
	else :
		print("Uncorrect password")
else :
	print("Uncorrect User name")

