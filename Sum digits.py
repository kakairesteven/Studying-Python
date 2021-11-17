# This program gets the sum of digits in a positive integer

def sumDigits(integer):
    if len(integer) == 1:   # Base condition
        return integer
    else:
        return int(integer[0]) + int(sumDigits(integer[1:]))


def main():
    integer = input("Enter integer: ")
    print("This is the sum of digits in", integer, "is", sumDigits(integer))


main()
