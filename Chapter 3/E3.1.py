
'''
(Geometry: area of a pentagon) Write a program that prompts the user to enter the
length from the center of a pentagon to a vertex and computes the area of the pentagon,
'''

# Import dependencies
import math
# Variable
length = eval(input("Enter the length from the center to the vertex: "))

# Computer the length of the side
s = 2*length*math.sin(math.pi/5)
area = (3*math.sqrt(3)*math.pow(s, 2)) / 2

print("The area of the pentagon is %.2f"%(area))
