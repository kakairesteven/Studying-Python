'''
(Convert pounds into kilograms) Write a program that converts pounds into
kilograms. The program prompts the user to enter a value in pounds, converts it to
kilograms, and displays the result. One pound is 0.454 kilograms
'''

pounds = eval(input("Enter a value in pounds: "))

kilogramValue = pounds * 0.454
print("%.1f pounds is %.3f kilograms"%(pounds, kilogramValue))
