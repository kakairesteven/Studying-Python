import random, time

# Set up the constants:
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3 # - 3 for room to enter the sum at the bottom


# The duration is in seconds:
QUIZ_DURATION = 1 # (!) Try changing this to 10 0r 60.
MIN_DICE = 2 # (!) Try changing this to 1 or 5.
MAX_DICE = 6 # (!) Try changing this to 14.

# (!) Try changing these to different numbers:
REWARD = 4 # (!) Points awarded for correct answers.
PENALTY = 1 # (!) Points removed for incorrect answers.
# (!) Try setting PENALTY to a negative to give points for
# wrong answers!

# The program hangs if all of the dice can't fit on the screen:
assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   0   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| 0     |',
        '|       |',
        '|     0 |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     0 |',
        '|       |',
        '| 0     |',
        '+-------+'], 2)


D3a = (['+-------+',
        '| 0     |',
        '|   0   |',
        '|     0 |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     0 |',
        '|   0   |',
        '| 0     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| 0   0 |',
       '|       |',
       '| 0   0 |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| 0   0 |',
       '|   0   |',
       '| 0   0 |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| 0   0 |',
        '| 0   0 |',
        '| 0   0 |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| 0 0 0 |',
        '|       |',
        '| 0 0 0 |',
        '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]
print('''Dice Math

Add up the sides of all the dice displayed on the screen.
You have {} seconds as many as possible. You get {} points for
each correct answer and lose {} point for each incorrect answer.

'''.format(QUIZ_DURATION, REWARD, PENALTY))

input('Press Enter to begin...')

# Keep track of how many answers were correct and incorrect:
correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()

while time.time() < startTime + QUIZ_DURATION: # Main game loop.
    # Come up with the dice to display:
    sumAnswer = 0
    dieFaces = []
#     die = random.choice(ALL_DICE)
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        # print('Die', die)
        # die[0] contains the list of strings on the face.
        dieFaces.append(die[0])
        # print('dieFaces', diceFaces)
        # die[1] contains the integer number of pips on the face:
        sumAnswer += die[1]    
    # print(sumAnswer)

    # Contain (x, y) tuples of the top-left corner of each die.
    topLeftDiceCorners = []
    # Figure out where dice should go:
    for i in range(len(dieFaces)):
        while True:
                # Find a random place on the canvas to put the die:
                left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
                top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)


                # Get the x, y coordinates for all four corners:
                #   left
                #   v
                #top > +-------+  ^
                #      | 0     | |
                #      |   0   | DICE_HEIGHT (5)
                #      |     0 | |
                #      +-------+ V
                #      <------->
                #      DICE_WIDTH (9)
                topLeftX = left
                topLeftY = top
                topRightX = left + DICE_WIDTH
                topRightY = top
                bottomLeftX = left
                bottomLeftY = top + DICE_HEIGHT
                bottomRightX = left + DICE_WIDTH
                bottomRightY = top + DICE_HEIGHT
                # print(topLeftX, topLeftY, topRightX, topRightY, bottomLeftX, bottomRightY, bottomRightX, bottomRightY)

                # Check if this die overlaps with previous dice.
                overlaps = False
                for prevDieLeft, prevDieTop in topLeftDiceCorners:
                        # print(prevDieLeft, prevDieTop)
                        prevDieRight = prevDieLeft + DICE_WIDTH
                        prevDieBottom = prevDieTop + DICE_HEIGHT

                        # print(prevDieLeft, prevDieTop)
                        # # Check each corner of this die to see if it is inside
                        # # of the area of  the previous die.
                        for cornerX, cornerY in ((topLeftX, topLeftY),
                                                (topRightX, topRightY),
                                                (bottomLeftX, bottomLeftY),
                                                (bottomRightX, bottomRightY)):
                                # print(cornerX, cornerY)
                                if (prevDieLeft <= cornerX < prevDieRight and
                                        prevDieTop <= cornerY < prevDieBottom):
                                        overlaps = True
                                        # print("Overlaps", overlaps)
                if not overlaps:
                        # It doesn't overlap, so we can put it here:
                        topLeftDiceCorners.append((left, top))
                        break
        # print(topLeftDiceCorners)
   # Draw the dice on the canvas:
   # keys are (x, y) tuples of ints, values the character at that
   # position
    canvas = {}
    # Loop over each die:
    for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
        # Loop over each character in the die's face:
        dieFace = dieFaces[i]
        # print(diceFace)
        for dx in range(DICE_WIDTH):
                for dy in range(DICE_HEIGHT):
                        # Copy this character to the correct place on the canvas:
                        canvasX = dieLeft + dx
                        canvasY = dieTop + dy
                        # Note that in dieFace, a list of strings, the x and y
                        # are swapped:
                        canvas[(canvasX, canvasY)] = dieFace[dy][dx]

    # Display the canvas on the screen:
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
                print(canvas.get((cx, cy), ' '), end='')
        print()
    
    # Let the player enter their answers:
    response = input('Enter the sum: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
            correctAnswers += 1
    else:
            print('Incorrect, the answer is', sumAnswer)
            time.sleep(2)
            incorrectAnswers += 1

# Display the final score
score = (correctAnswers * REWARD) - (incorrectAnswers * PENALTY)
print('Correct: ', correctAnswers)
print('Incorrect: ', incorrectAnswers)
print('Score: ', score)
