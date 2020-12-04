##################################################
###   Author      : Doaa Maher                ####
###   File 		  : CSV File dict reading     ####
###   Date        : 4 Dec 2020                ####
###   Version     : 1.0                       ####
##################################################

import csv
reader = csv.reader( open ('simplecsv.csv' , 'r') )

mydict = {}

for line in reader :
	mydict[line [0] ] = { 'ID' : line [1] , 'Color' : line [2] }

print(mydict)