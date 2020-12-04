##################################################
###   Author      : Doaa Maher                ####
###   File 		  : Uses of memoryview	      ####
###   Date        : 4 Dec 2020                ####
###   Version     : 1.0                       ####
##################################################


#The memoryview() function returns a memory view object of the given argument this is done via Python Buffer Protocol
#The buffer protocol allows one object to expose its internal data (buffers) and the other to access those buffers without intermediate copying.

byte_array = bytearray('XYZ', 'utf-8') 
print('Before update:', byte_array) 
  
mem_view = memoryview(byte_array) 
  
# update 2nd index of mem_view to J  
mem_view[2]= 74
print('After update:', byte_array)


import time
for n in (100000, 200000, 300000, 400000):
    data = 'x'*n
    start = time.time()
    while data:
        data = data[1:]
    print ('bytes', n, time.time()-start)
    

for n in (100000, 200000, 300000, 400000):
    data = 'x'*n
    start = time.time()
    data=bytearray(data,'utf-8')
    data = memoryview(data)
    while data:
        data = data[1:]
    print ('memoryview', n, time.time()-start)