'''
(Compute the volume of a cylinder) Write a program that reads in the radius and
length of a cylinder and computes the area and volume using the following formulas:
area = radius * radius * π
volume = area * length
'''
from math import pi
PI = pi

radius, height = eval(input("Enter the radius and height of the cylinder: "))
area = 2 * pi * radius * height
volume = pi * pow(radius, 2) * height

# integer formatting / precision
print("The area of the cylinder is %.3f and the volume is %.3f"%(area, volume))