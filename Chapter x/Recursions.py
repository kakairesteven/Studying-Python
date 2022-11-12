# Calculating factorials

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


integer = int(input("Enter number: "))
print("The factorial of", integer, "is", factorial(integer))
