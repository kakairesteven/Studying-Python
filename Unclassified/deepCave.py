import time, sys, random

WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Press Ctrl-C to stop.')
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
    # Display the tunnel segment:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))
    # Check for Ctrl-C during the brief pause:
    try:
        time.sleep(PAUSE_AMOUNT) # PAUSE_AMOUNT must be non-negative.
    except KeyboardInterrupt: # When Ctrl-C is pressed, end the program.
        sys.exit()

    """ # Adjust the left side width:
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth -= 1 # Decrease left side width
    elif diceRoll == 2 and (leftWidth + gapWidth) < WIDTH - 1:
        leftWidth += 1
    else:
        pass # do nothing, no change in the left side width.
 """
    # Adjust the gap width
    # (!) Try uncommenting out all of the following code:
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and gapWidth > 1:
        gapWidth -= 1 # Decrease gap width.
    elif diceRoll == 2 and (leftWidth + gapWidth) < WIDTH - 1:
        gapWidth += 1 # Increase gap width.
    else:                                           
        pass # Do nothing; no change in gap width.