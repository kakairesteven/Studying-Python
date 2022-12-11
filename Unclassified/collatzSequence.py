# If n is even, the next number n is n/2
# If n is odd, the next number n is n * 3 + 1
# If n is 1, stop. Otherwise, repeat.

# Prompt user to enter an integer
while True:
    number = input('Please enter a positive integer: ')
    if number.isdecimal() and number != 0:
        number = int(number)
        print('n = {}'.format(number))
        break
    else:
        print('Invalid input. Please enter a valid number: ')
print(number, end=' ')
while True: # Loop until n is 1
    if number == 1:
        break
    elif number % 2 == 0:
        # number = round(number / 2)
        number = number // 2
        print(number, end=' ')
    else:
        number = number * 3 + 1
        print(number, end=' ')
