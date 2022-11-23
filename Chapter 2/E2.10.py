import math
# minimum run-way length
speed, acceleation = eval(input("Enter the speed \
    and acceleration of the plane: "))

length = math.pow(speed, 2) / (2*acceleation)
print("The minimum runway length for \
    the airplane is %.3f meters"%(length))
