# Surface area of a cylinder 

#Measurements
#2 pi r2 +2pi dh
print("Input the following ")
print ("Enter PI measurements")
pi= float (input())
print("Enter the Radius")
rad =int(input())
print(" Enter the Height")
height= int (input())

#SA of closed Cylinder 
#2pi r2 + 2pi dh
surf_area =2*(pi *rad*rad) +2*pi* (rad +rad)*height
print ("The surface area is" , surf_area)

#Open Tank 
#pi r2 +pi dh
open =(pi* rad*rad) +pi*(rad*rad)*height
print("The surface area of the tank is" , open)

#Pipe
#pi dh
pipe=pi*(rad*2)*height
print("the surface area of the pipe is" , pipe)