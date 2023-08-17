#Area , Perimeter and volume of a cube

#We prompt the user to give the measurements 

#Measurements 
print("kindly fill the information")
print("Length")
len=int(input())
print("Width")
wid=int(input())
print("Height")
hgt=int(input())

#Perform the perimeter
per= 2*(len+wid)
print(per)

#perform area
area=len*wid
print(area)

#perform volume 
vol=len*wid*hgt
print(vol)