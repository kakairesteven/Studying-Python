def m(i):
    if i == 1:
        return float(1)
    else:
        return float(1/m(i-1)) + float(1 / i)


def main():
    i = float(input("Enter i: "))
    print(m(i))


main()
