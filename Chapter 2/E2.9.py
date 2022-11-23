import math
while True:
    outer_temp = eval(input("Enter the outside temperature: "))
    wind_speed = eval(input("Enter the velocity of wind in miles per hour: "))

    if -58 < outer_temp < 41 and wind_speed >= 2:
        break
    else:
        continue

wind_chill_temp = 35.74 + 0.6215*outer_temp \
    - 35.75*math.pow(wind_speed, 0.16) \
    + 0.4275*outer_temp*math.pow(wind_speed, 0.16)

print("The wind-chill temperature is %.5f"%(wind_chill_temp))
