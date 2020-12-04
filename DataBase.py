##################################################
###   Author      : Doaa Maher                ####
###   File 		  : DataBase			      ####
###   Date        : 4 Dec 2020                ####
###   Version     : 1.0                       ####
##################################################


Name_list = ["ahmed","ali",'amr','doaa']
Sal_list  = [2000, 3000, 4000, 5000]


Name = input("Please Enter Employee Name: ")
Name = Name.lower() # To make sure all in lower Cases

index = 0
for x in Name_list:
	if x == Name:
		print(Sal_list[index])
	index = index + 1