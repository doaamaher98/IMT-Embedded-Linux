##################################################
###   Author      : Doaa Maher                ####
###   File 		  : Numpy Library 		      ####
###   Date        : 4 Dec 2020                ####
###   Version     : 1.0                       ####
##################################################

'''
To install, open your terminal 
pip install numpy 

to update your pip
python -m pip install --upgrade pip
################################
'''
import numpy

arr = numpy.array([1, 2, 3, 4, 5])
arr[1] = 12
print(arr)
print(type(arr))

################################
#Create 2-D array with numpy library

import numpy as np #Text replacement
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
################################

#check the dimensions 
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
#################################
#accessing 2-D arrayimport numpy as np

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st dim: ', arr[0, 1])

print('5th element on 2nd dim: ', arr[1, 4])
1 2 3 4 5
6 7 8 9 10
################################
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2]) 
think about the output ?!
################################
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])
print('Last element from 2nd dim: ', arr[1, 4])