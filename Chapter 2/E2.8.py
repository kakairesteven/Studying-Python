'''
(Science: calculate energy) Write a program that calculates the energy needed to
heat water from an initial temperature to a final temperature. Your program should
prompt the user to enter the amount of water in kilograms and the initial and final
temperatures of the water. The formula to compute the energy is
Q = M * (finalTemperature – initialTemperature) * 4184
where M is the weight of water in kilograms, temperatures are in degrees Celsius,
and energy Q is measured in joules.
'''

mass = eval(input("Enter the mass of the water in kilograms: "))
initial_temp = eval(input("Enter the initial temperature in celcius: "))
final_temp = eval(input("Enter the final temperature in celcius: "))

energy = mass * (final_temp - initial_temp) * 4184

print("Energy used to heat %.1f kilograms of water from %.1f degrees to %.1f degrees is %.1f joules"%(mass, initial_temp, final_temp, energy))