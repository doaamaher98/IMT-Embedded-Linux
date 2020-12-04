##################################################
###   Author      : Doaa Maher                ####
###   File 		  : Printing age from user    ####
###   Date        : 4 Dec 2020                ####
###   Version     : 1.0                       ####
##################################################




Age = input("Please enter your birth year: ")
Age = int(Age)
Years = 2020 - Age
Years = str(Years)
Message = "You are " + Years + " Years Old"
print(Message)