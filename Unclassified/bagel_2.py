import random

from scipy import rand
guessDigits = 3
attempts = 10

def check(guess, secretNumber):
    clues = ''
    for i in range(len(guess)):
        if guess[i] == secretNumber[i]:
            clues += 'Fermi '
        elif guess[i] in secretNumber:
            clues += 'Pico '
        elif guess[i] not in secretNumber:
            clues += 'Bagel '
    return clues

def generateSecretNumber():
    numList = list('0987654321')
    
    random.shuffle(numList)
    secretNumber = ''
    numberOfGuesses = 0
    while numberOfGuesses < (guessDigits):
        # secretNumber.append(random.shuffle(numList)[i])
        secretNumber += str(numList[numberOfGuesses])
        numberOfGuesses += 1
    return secretNumber

def main():
    while True:
        # constants
        secretNumber = generateSecretNumber()
        print(secretNumber)
        guesses = 1

        # keep looping until they enter a valid guess
        while guesses <= attempts:
            guess = ''
            while len(guess) != guessDigits or not guess.isdecimal():
                guess = input("Guess {}: ".format(guesses))
                print(check(guess, secretNumber))
                guesses += 1

        # Ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing!')
main()
