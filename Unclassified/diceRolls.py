import random, sys
# Ask for user input of the diceStr
while True:
    print('Enter dice string or quit!')
    diceStr = input('> ')
    print(diceStr)

    if diceStr.isalpha() and diceStr.upper() == 'QUIT':
        print('Thanks for playing!')
        sys.exit()

    # Check for input validity
    if diceStr.find('d') == -1:
        raise Exception("Invalid input, missing the 'd' character")

    else:
        dIndex = diceStr.index('d')
        rollsNumber = diceStr[:dIndex]
        print("dIndex: {} diceRolls: {}".format(dIndex, rollsNumber))

    if rollsNumber.isdecimal():
        rollsNumber = int(rollsNumber)
    else:
        raise Exception('The rolls number is invalid')

    if '-' in diceStr:
        modeIndex = diceStr.index('-')
        diceFaces = int(diceStr[dIndex+1:modeIndex]) - int(diceStr[modeIndex:])
        print('diceFaces: {}'.format(diceFaces))
    elif '+' in diceStr:
        modeIndex = diceStr.index('+')
        diceFaces = int(diceStr[dIndex+1:modeIndex]) + int(diceStr[modeIndex:])
        print('diceFaces: {}'.format(diceFaces))
    else:
        diceFaces = int(diceStr[dIndex+1:])

    # Roll dice
    rollSum = 0
    rolls = []
    for i in range(rollsNumber):
        rolledFaces = random.randint(1, diceFaces)
        rolls.append(rolledFaces)
    rollSum = sum(rolls)

    print("Dice Rolls", rolls)

    response = input('Enter sum of the dice faces: \n>: ')
    if response.isdecimal():
        response = int(response)
    else:
        raise Exception('Invalid response')

    if response == rollSum:
        print('Wow')
        break
    else:
        print('Incorrect answer. Sum is {}'.format(rollSum))
