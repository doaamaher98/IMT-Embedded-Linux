##################################################
###   Author      : Doaa Maher                ####
###   File 		  : Binary Search		      ####
###   Date        : 4 Dec 2020                ####
###   Version     : 1.0                       ####
##################################################


# Creating the list
myList = []
List_Items = int(input("Enter the number of elements in the list : "))
# Filling up the list by the user
for i in range(List_Items):
    List = int(input("Enter The List : "))
    myList.append(List)

# Printing the list
print("Your List is :")    
print(myList)

# Sorting the list in ascending order
myList.sort()
print("Your List after sortion is : ") 
print(myList)

# Searching for the Key
Key = int(input("Enter the Key you're looking for : "))

# The Binary Search :
low_index = 0
high_index = List_Items -1

while(low_index <= high_index):
    mid = (low_index + high_index) // 2
    if(Key == myList[mid]):
        print(Key , "Is Found in the List")
        break
		
    elif (Key > myList[mid]):
        low_index = high + 1
    elif(Key < myList[mid]):
        high_index = mid - 1


		