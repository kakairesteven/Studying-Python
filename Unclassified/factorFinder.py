import sys, math

while True:
    print('''
    INSTRUCTIONS
    1. Enter a positive number to find its factors.
    2. Or press 'Q' to quit''')
    response = input('> ')

    if response.upper() == 'QUIT':
        sys.exit()

    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors = []

    # Find the factors of number:
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i) 

    factors = list(set(factors)) # Remove duplicates
    factors.sort() # Sort factors in order

    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(', '.join(factors))
