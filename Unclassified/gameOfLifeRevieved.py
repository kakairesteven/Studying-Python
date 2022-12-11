import random, copy, sys, time

WIDTH = 35
HEIGHT = 15
ALIVE = '0'
DEAD = ' '

def generateCells(width, height):
    cells = {}
    for x in range(width):
        for y in range(height):
            cells[(x, y)] = random.choice([ALIVE, DEAD])
    return cells

while True: # main loop
    print('\n' * 10)
    # generateCells(WIDTH, HEIGHT)
    cells = generateCells(WIDTH, HEIGHT)

    # print cells
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)],  end='')
        print()

    newCells = copy.deepcopy(cells)
    
    # Neighbors for agiven cell at (x, y)
    numNeighbors = 0
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # Neighboring cell co-ordinates
            # Wrap around edge of the window.
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT
            

            if newCells[(left, above)] == ALIVE: 
                numNeighbors += 1
            if newCells[(left, y)] == ALIVE:
                numNeighbors += 1
            if newCells[(left, below)] == ALIVE:
                numNeighbors += 1
            if newCells[(x, above)] == ALIVE:
                numNeighbors += 1
            if newCells[(x, below)] == ALIVE:
                numNeighbors += 1
            if newCells[(right, y)] == ALIVE:
                numNeighbors += 1
            if newCells[(right, above)] == ALIVE:
                numNeighbors += 1
            if newCells[(right, below)] == ALIVE:
                numNeighbors += 1

        # Check and determine survival and life of a cell
        if 2 <= numNeighbors <= 3 and newCells[(x, y)] == ALIVE:
            newCells[(x, y)] = ALIVE
        if numNeighbors == 3 and newCells[(x, y)] == DEAD:
            newCells[(x, y)] = ALIVE
        else:
            newCells[(x, y)] = DEAD
    
    # print(cells)
    print('\n' * 5)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(newCells[(x, y)],  end='')
        print()

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()