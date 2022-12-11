from getHandValue import getHandValue
from deck import getDeck

BACKSIDE = 'backside'

def displayHands(playerHand, DealerHand, showDealerHand):
    print()
    # If showDealerHand is true, display dealerHand cards
    # else hide the dealerHand cards
    if showDealerHand: 
        print('DEALER: ', getHandValue(DealerHand))
        displayCards(DealerHand)
    else: # This displays the backside of a card.
        print('DEALER: ???')
        displayCards([BACKSIDE] + DealerHand[1:])
    # Display player cards
    print('PLAYER: ', getHandValue(playerHand))
    displayCards(playerHand) # displaycards displays cards a player holds


def displayCards(cards):
    rows = ['', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += '  __  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    print(rows)
    for row in rows:
        print(row)

deck = getDeck()[0:4]
print(len(deck))
displayCards(deck) 
