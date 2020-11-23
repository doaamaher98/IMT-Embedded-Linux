# bytes  converts an object to immutable byte represented object of given size and data.
empty_bytes =bytes(4)
print(empty_bytes)
print(type(empty_bytes))

data=bytes(b'\xFF\xFF')
print(data)
data=bytes(b'\xFF\xFF')
data[0]=1
print(data)

#convert list to bytes
rList = [1, 2, 3, 4, 5]
arr = bytes(rList)
print(arr)

str1 = 'HellÖrHeaven'  
# Giving ascii encoding and ignore error 
print ("Byte conversion with ignore error : " +
      str(bytes(str1, 'ascii', errors = 'ignore')))  
  
# Giving ascii encoding and replace error 
print ("Byte conversion with replace error : " +
      str(bytes(str1, 'ascii', errors = 'replace')))  
  
# Giving ascii encoding and strict error 
# throws exception 
print ("Byte conversion with strict error : " +
      str(bytes(str1, 'ascii', errors = 'strict')))
      
data="\x68\x65\x6c\x6c\x6f"
print ("Byte conversion with ignore error : " +
      str(bytes(data, 'ascii', errors = 'ignore')))  
      
#bytearray
mutable_empty_bytes =bytearray(4)
print(mutable_empty_bytes)
print(type(mutable_empty_bytes))

mutable_empty_bytes =bytearray(b'\xF1\xF2\xF3\xF4')
print(mutable_empty_bytes)
print(type(mutable_empty_bytes))

mutable_empty_bytes =bytearray(b'\xF1\xF2\xF3\xF4')
mutable_empty_bytes[0]=0
mutable_empty_bytes.append(255)
print(mutable_empty_bytes)
print(type(mutable_empty_bytes))