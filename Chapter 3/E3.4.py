import math

lengthSide = eval(input("Enter the side: "))

# Compute area
area = (5*math.pow(lengthSide, 2)) / (4*math.tan(math.pi/5))

# Print output
print("The area of the pentagon is %.10f"%(area))