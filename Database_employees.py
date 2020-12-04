##################################################
###   Author      : Doaa Maher                ####
###   File 		  : DataBase			      ####
###   Date        : 4 Dec 2020                ####
###   Version     : 1.0                       ####
##################################################
##################################################
# Database to :
#				1- Add a new employee
#				2- Print the employee data
#				3- Remove employee from the system	
#########################################################
DataBase_dict = dict();

while 1:
	print("|***********************************************|")
	print("| To Add New Empolyee Press 1                   |")
	print("| To Print Employee Data press 2                |")
	print("| To Delete Employee Press 3                    |")
	print("|***********************************************|")
	
	choice = input("Please enter your choice: ")
	if int(choice) == 1:
		ID = input("Please enter employee ID: ")
		while int(ID) in DataBase_dict:
			ID = input("ID already exist, please try another one: ")
		name   = input("Please Enter Employee Name: ")
		job    = input("Please Enter Employee Job : ")
		salary = input("Please Enter Employee Salary : ")
		
		DataBase_dict[int(ID)] = dict(Name=name,Job=job,Salary=salary)
	
	elif int(choice) == 2:
		ID = input("Please enter employee ID: ")
		if int(ID) in DataBase_dict:
			print("Employee Name  : " + str(DataBase_dict[int(ID)]['Name']))
			print("Employee Job   : " + str(DataBase_dict[int(ID)]['Job']))
			print("Employee Salary: " + str(DataBase_dict[int(ID)]['Salary']))
		else:
			print("Employee Not Found")
	elif int(choice) == 3:
		ID = input("Please enter employee ID: ")
		if int(ID) in DataBase_dict:
			DataBase_dict.pop(int(ID))
			print("Employee Deleted")
		else:
			print("Employee Not Found")
		
	else:
		print("Wrong Choice, Please try again")