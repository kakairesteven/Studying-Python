import sys
def getBet(maxBet):
    while True:
        print('How much do you want to bet? 1. {} 0-QUIT'.format(maxBet))
        bet = input('> ')
        if bet.upper().strip() == 'QUIT':
            print('Thanks for playing.')
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1<= bet <= maxBet:
            return bet

# getBet(50000)
