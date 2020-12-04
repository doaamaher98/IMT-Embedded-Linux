##################################################
###   Author      : Doaa Maher                ####
###   File 		  : Loan with installment     ####
###   Date        : 4 Dec 2020                ####
###   Version     : 1.0                       ####
##################################################


Loan  = float(input("Please enter the loan value: "))
Years = float(input("Please enter the number of Years: "))

Value = Loan * ((Years * 0.12) + 1)
Installment = Value / (12*Years)

Installment = str(Installment)
print("Your monthly Installment is " + Installment)