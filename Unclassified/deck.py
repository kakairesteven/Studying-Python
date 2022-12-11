import random

HEARTS = chr(9829) # Character 9829 is '❤️'
DIAMONDS = chr(9830) # Character 9830 is '♦️'
SPADES = chr(9824) # Character 9824 is '♠️'
CLUBS = chr(9827) # Character 9827 is '♣️'

def getDeck():
    deck = []
    for i in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for j in range(2, 11):
            deck.append((str(j), i))
        for  j in ('J', 'Q', 'K', 'A'):
            deck.append((j, i))
    random.shuffle(deck)
    # print(deck)
    return deck
    
getDeck()


deck = getDeck();
print(deck)

playerHand = [deck.pop(), deck.pop()]
dealerHand = [deck.pop(), deck.pop()]
print(playerHand)
print(dealerHand)
