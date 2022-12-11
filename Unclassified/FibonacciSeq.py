import sys, time
# Prompt user to enter an input
# Check entered input

while True:
    while True:
        print('''
        Enter an integer greater than 0 to calculate its Fibonacci number.
        Or type 'QUIT' to quit.
        ''')

        response = input('> ')
        if response.upper() == 'QUIT':
            print('Exiting ...')
            time.sleep(3)
            sys.exit()

        elif response.isdecimal() and int(response) != 0:
            nth = int(response)
            break
        print()

    if nth == 1:
        print('0, 1')
        print('The Fibonacci number calculated is 1')


    elif nth == 2:
        print('0, 1')
        print('The # 2 Fibonacci number calculated is 1.')

    elif nth > 10_000:
        print(
        '''
        This is a large number. It shall take a while to
        calculate display the fibonacci  numbers.''')
        print('''
        To exit, press Ctrl+C''')
        print('Press Enter to begin.')

    # Calculate the nth number.
    lastNumber = 1
    secondLastNumber = 0
    fibNumberCalculated = 2
    print('0, 1, ', end='')
    # Calculate fibonacci number
    while True:
        nextNumber = secondLastNumber + lastNumber
        fibNumberCalculated += 1
        print(nextNumber, end='')
        if nth == fibNumberCalculated:
            print()
            print()
            print('The # ', fibNumberCalculated, ' Fibonacci ', 
                'number is ', nextNumber, sep='')
            break
        # print a comma in between the sequence numbers
        print(', ', end='')
        secondLastNumber = lastNumber
        lastNumber = nextNumber