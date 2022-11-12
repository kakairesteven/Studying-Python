"""
(Financial application: calculate tips) Write a program that reads the subtotal and
the gratuity rate and computes the gratuity and total. For example, if the user
enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
as the gratuity and 11.5 as the total.
"""

# Total = subtotal + gratuity

# Prompt user to enter subtotal and gratuity
subtotal, gratuity = eval(input("Enter the subtotal and a gratuity percentage: "))
gratuityAmount = (gratuity * subtotal) / 100
total = subtotal + gratuityAmount

# Output the gratuity and total
print("The gratuity is %.2f and the total is %.2f"%(gratuityAmount, total))
