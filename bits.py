#Bits operations 
#3 methods of Bit OPerations
#In each method we will use 2 concepts
#we will use user defined functions 
#we will use Program Built functions 

#Method 1
#The inbuilt function is DecimalToBinary()
#bin()

#user defined function 
#(key word) def...()
#     return()

#DecimalToBinary
def DecimalToBinary(n): #function definition
    return(" { 0:b}" .format(int(n)) )

#Function call 1
d =DecimalToBinary(9)
#print(d)

#Function call 2
s =DecimalToBinary(546)
#print(s)

#Bin Function
t =bin(14) #Quick Ninja way 
#print(t)

#Second Escapade 
r= bin(789)
print(r)
