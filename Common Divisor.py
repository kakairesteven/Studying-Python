def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


def main():
    m = int(input("Enter m: "))
    n = int(input("Enter n: "))
    print("The greatest common divisor of", m, "and", n, "is", gcd(m, n))


main()
