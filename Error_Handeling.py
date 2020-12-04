##########################################################
###   Author      : Doaa Maher               		  ####
###   File 		  : Checking if file was existed      ####
###   Date        : 4 Dec 2020                		  ####
###   Version     : 1.0                               ####
##########################################################
try :
	file = open("missingfile.txt" , "r")
except FileNotFoundError :
	print("File isn't found!")