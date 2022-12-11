import random, sys, bext, time
# CONSTANTS
WIDTH = 79
HEIGHT = 22

TREE = '🌳'
FIRE = '🔥'
EMPTY = ' '

INITIAL_FOREST_DENSITY = 0.20
FIRE_CHANCE = 0.01
GROW_CHANCE = 0.01
PAUSE_LENGTH = 0.5


def getForest():
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random()) <= INITIAL_FOREST_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY
    return forest


def displayForest(forest):
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            else:
                print(EMPTY, end='')
        print()
    bext.fg('reset')


def main():
    forest = getForest()
    # print(getForest())

    while True:
        displayForest(forest)
        newForest = {'width': forest['width'], 'height': forest['height']}
        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in newForest:
                    continue
                if (forest[(x, y)] == EMPTY) and random.random() <= GROW_CHANCE:
                    newForest[(x, y)] = TREE
                elif (forest[(x, y)] == TREE) and random.random() <= FIRE_CHANCE:
                    # There must be a tree to catch fire
                    newForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # loop through the neighboring trees to spread the fire
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # If there is a tree, burn it
                            if forest.get((x + ix, y + iy)) == TREE: # Returns a value for a specific key,
                                # none if not found, instead of an error.
                                # Tree is burns down
                                newForest[(x + ix, y + iy)] = FIRE
                    newForest[(x, y)] = EMPTY
                else:
                    newForest[(x, y)] = forest[(x, y)]
        forest = newForest
        time.sleep(PAUSE_LENGTH)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()