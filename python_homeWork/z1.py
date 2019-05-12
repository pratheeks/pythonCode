print("-------------------\n1]")
"""print the string in a specific format"""
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

print("-------------------\n2]")
"""printing the version of python"""
import sys
print("python version")
print(sys.version)
print("version info")
print(sys.version_info)

print("-------------------\n3]")
"""printing the data&time of system"""
import datetime
now=datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

print("-------------------\n4]")
"""calculating the area of circle"""
from math import pi
r=float(input("Enter the radius of circle!"))
print("The area of circle of radius "+str(r)+"is"+str(pi*r**2))
