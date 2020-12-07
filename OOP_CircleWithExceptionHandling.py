##############################################################
###   Author      : Doaa Maher               		  	  ####
###   File 		  : Finding Area,Circum of Circle		  ####
###   Date        : 6 Dec 2020                		  	  ####
###   Version     : 1.0                               	  ####
##############################################################
class Circle():
    def __init__(self):
        try:
            self.radius = int(input("Please enter your radius: "))
            if self.radius < 0:
                raise TypeError("Only integers are allowed")
        except TypeError :
            print("Invalid radius was intered")
            exit()

    def area(self):
        return self.radius**2*3.14
    
    def Cirum(self):
        return 2*self.radius*3.14

NewCircle = Circle()
print(NewCircle.area())
print(NewCircle.Cirum())