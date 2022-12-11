import random, time, shutil, sys

LEFT = 'left'
RIGHT = 'right'
OPEN = 'open'
CLOSED = 'closed'
BEADY = 'beady'
CHUBBY = 'chubby'
HAPPY = 'happy'
VERY_CHUBBY = 'very chubby'
WIDE = 'wide'
ALOOF = 'aloof'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

DENSITY = 0.10
DUCKLING_WIDTH = 5
PAUSE = 0.2

def main():
    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            if (ducklingObj == None and random.random() <= DENSITY):
                ducklingObj = Duckling()
                ducklingLanes[laneNum] = ducklingObj

            if ducklingObj != None:
                print(ducklingObj.getNextBodyPart(), end='')
                if ducklingObj.partToDisplayNext == None:
                    ducklingLanes[laneNum] = None
            else:
                print(' ' * DUCKLING_WIDTH, end='')
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)


class Duckling:
    def __init__(self):
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])
        self.partToDisplayNext = HEAD


    def getHeadStr(self):
        # direction
        headStr = ''
        if self.direction == LEFT:
            if self.mouth == OPEN:
                headStr += '>'
            elif self.mouth == CLOSED:
                headStr += '='

            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += '" '
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'
            headStr += ') '

        if self.direction == RIGHT:
            headStr += ' (' # Get the back of the head.

            # Get the eyes:
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += ' "'
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'
            # headStr += ' '

            # Get the mouth:
            if self.mouth == OPEN:
                headStr += '<'
            elif self.mouth == CLOSED:
                headStr += '='

        if self.body == CHUBBY:
            headStr += ' '
        
        # headStr += ') '
        return headStr


    def getBodyStr(self):
        bodyStr = '('
        if self.direction == LEFT:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

            # Get the wing:
            if self.wing == OUT:
                bodyStr += '>'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'
  
        if self.direction == RIGHT:
            # Get the wing:
            if self.wing == OUT:
                bodyStr += '<'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

            # Get the interior body space:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

        bodyStr += ')'

        if self.body == CHUBBY:
            bodyStr += ' '

        return bodyStr

    def getFeetStr(self):
        if self.body == CHUBBY:
            return ' ^^  '
        elif self.body == VERY_CHUBBY:
            return ' ^ ^ '

    def getNextBodyPart(self):
        if self.partToDisplayNext == HEAD:
            self.partToDisplayNext = BODY
            return self.getHeadStr()
        elif self.partToDisplayNext == BODY:
            self.partToDisplayNext = FEET
            return self.getBodyStr()
        elif self.partToDisplayNext == FEET:
            self.partToDisplayNext = None
            return self.getFeetStr()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()