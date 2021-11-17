def f(n):
    if n == 1:
        return 1
    else:
        return n + f(n-1)


number = int(input("Enter number: "))
print("Sum of integers up to", number, "is", f(number))
