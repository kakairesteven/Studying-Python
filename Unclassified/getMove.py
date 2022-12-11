def getMove(playerHand, money):
    while True: # Loop until player enters a valid move.
        moves = ['(H)it', '(S)tand']

        # if playerHand has two cards and money is greater than zero,
        # the player can (D)ouble down.
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
            movePrompt = ', '.join(moves) + '> '
            move = input(movePrompt).upper()
            if move in ('H', 'S'): # Get the player's move
                return move # Return move
            if move == 'D' and '(D)ouble down' in moves:
                return move # Return move