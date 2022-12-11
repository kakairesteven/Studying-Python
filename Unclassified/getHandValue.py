def getHandValue(cards):
    numberOfAces = 0    # Initialize number of Aces
    value = 0   # Initializa hand value
    for card in cards:  
        rank = card[0]  # index rank of a card e.g 2 in (2, '❤️')
        if rank == 'A': # for aces, count number of aces.
            numberOfAces += 1
        elif rank in ('K', 'J', 'Q'): # Add 10 for ranks K, J, or Q
            value += 10
        else:   # for ranks 2 through 10, add rank's face value.
            value += 1
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value

