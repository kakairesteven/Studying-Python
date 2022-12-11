import shutil, sys

# Define chars
UP_DOWN = chr(9474)
LEFT_RIGHT = chr(9472)
DOWN_RIGHT = chr(9484)
DOWN_LEFT = chr(9488)
UP_RIGHT = chr(9492)
UP_LEFT = chr(9496)
UP_DOWN_RIGHT = chr(9500)
UP_DOWN_LEFT = chr(9508)
DOWN_LEFT_RIGHT = chr(9516)
UP_LEFT_RIGHT = chr(9524)
CROSS_CHAR = chr(9532)

ALL_CHARS = [
UP_DOWN, LEFT_RIGHT, DOWN_RIGHT,
DOWN_LEFT, UP_RIGHT, UP_LEFT, UP_DOWN_RIGHT,
UP_DOWN_LEFT, DOWN_LEFT_RIGHT, UP_LEFT_RIGHT,
CROSS_CHAR
]

# window size
WINDOW_WIDTH, WINDOW_HEIGHT = shutil.get_terminal_size()

WINDOW_WIDTH -= 1
WINDOW_HEIGHT -= 5

canvas = {}
canvasX = 0
canvasY = 0

def getCanvasStr(canvasData, x, y):
    canvasStr = ''
    for rowNum in range(WINDOW_HEIGHT):
        for columnNum in range(WINDOW_WIDTH):
            if rowNum == y and columnNum == x:
                canvasStr += '#'
                continue            
            cell = canvasData.get((columnNum, rowNum))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvasStr += UP_DOWN
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += LEFT_RIGHT
            elif cell == set(['A', 'S']):
                canvasStr += DOWN_LEFT
            elif cell == set(['S', 'D']):
                canvasStr += DOWN_RIGHT
            elif cell == set(['A', 'W']):
                canvasStr += UP_LEFT
            elif cell == set(['W', 'D']):
                canvasStr += UP_RIGHT
            elif cell == set(['W', 'S', 'D']):
                canvasStr += UP_DOWN_RIGHT
            elif cell == set(['W', 'S', 'A']):
                canvasStr += UP_DOWN_LEFT
            elif cell == set(['A', 'S', 'D']):
                canvasStr += DOWN_LEFT_RIGHT
            elif cell == set(['W', 'A', 'D']):
                canvasStr += UP_LEFT_RIGHT
            elif cell == set(['W', 'A', 'S', 'D']):
                canvasStr += CROSS_CHAR
            elif cell == None:
                canvasStr += ' '
        canvasStr += '\n'
    return canvasStr


moves = []
while True:
    # Prompt user to enter a response
    print(getCanvasStr(canvas, canvasX, canvasY))
    response = input('> ').upper()
    if response == 'QUIT' or response == 'Q':
        sys.exist()
    elif response == 'H':
        print('''
        INSTRUCTIONS:
        1. Press W, A, D, and/or D to move draw on the canvas.
        2. Press H + Enter for help.
        3. Type 'QUIT' and Press Enter or press 'Q' + enter to quit.
        4. Press F + Enter to save file.
        5. Press C + Enter to clear canvas.
        ''')
    elif response == 'C':
        canvas = {}
        continue
    elif response == 'F':
        try:
            print('Enter filename to save to:')
            filename = input('> ')
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(getCanvasStr(canvas, None, None))
        except:
            print('ERROR: Could not save file.')
            
    for command in response:
        if command not in ('W', 'S', 'A', 'D'):
            continue
        moves.append(command)
        if canvas == {}:
            if command in ('W', 'S'):
                canvas[(canvasX, canvasY)] = set(['W', 'S'])
            elif command in ('A', 'D'):
                canvas[(canvasX, canvasY)] = set(['A', 'D'])

        if command == 'W' and canvasY > 0:
            canvas[(canvasX, canvasY)].add(command)
            canvasY -= 1
        elif command == 'A' and canvasX > 0:
            canvas[(canvasX, canvasY)].add(command)
            canvasX -= 1
        elif command == 'D' and canvasX < WINDOW_WIDTH - 1:
            canvas[(canvasX, canvasY)].add(command)
            canvasX += 1
        elif command == 'S' and canvasY < WINDOW_HEIGHT - 1:
            canvas[(canvasX, canvasY)].add(command)
            canvasY += 1
        else:
            continue
        
        if (canvasX, canvasY) not in canvas:
            canvas[(canvasX, canvasY)] = set()
        if command == 'W':
            canvas[(canvasX, canvasY)].add('S')
        elif command == 'A':
            canvas[(canvasX, canvasY)].add('D')
        elif command == 'D':
            canvas[(canvasX, canvasY)].add('A')
        elif command == 'S':
            canvas[(canvasX, canvasY)].add('W')