##################################################
###   Author      : Doaa Maher                ####
###   File 		  : Swapping 2 numbers	      ####
###   Date        : 4 Dec 2020                ####
###   Version     : 1.0                       ####
##################################################

# Taking inputs from the user :

x = input('Enter value of x: ')
y = input('Enter value of y: ')

print("x =", x)
print("y =", y)

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

