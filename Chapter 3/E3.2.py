import math
# CONSTANTS

# Convert kilometers to meters
RADIUS = 6371.01

# Prompt user to enter point 1 and point 2
point1 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))
point2 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))

# Obtain x and y by indexing and convert to radians
x1 = math.radians(point1[0])
y1 =  math.radians(point1[1])

x2 = math.radians(point2[0])
y2 = math.radians(point2[1])

GreaterCircleDistance = RADIUS*math.acos(math.sin(x1)*math.sin(x2) + math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
print("The distance between the two points is %.5f km"%(GreaterCircleDistance))