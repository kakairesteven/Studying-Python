# Zeno's paradox code


def zeno(integer):
    if integer != 0:
        integer = integer / 2
        return integer
    else:
        return integer


'''
n = input("Enter n: ")
print(zeno(n))
'''


# looped version
count = 0
n = float(input("Enter number: "))

results = []
while count != 10000000000:
    count += 1
    n = n / 2
    results.append(n)

print(count, results, len(results))
