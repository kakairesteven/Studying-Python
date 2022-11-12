# This program prints a message n times

def nPrint(message, n):
    if n >= 1:
        print(message)
        nPrint(message, n - 1)


# prompt
message = input("Enter message: ")
number = int(input("Enter n: "))
print(nPrint(message, number))
