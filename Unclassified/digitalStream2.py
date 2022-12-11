import sys, time, random, shutil

# Constants
WIDTH = shutil.get_terminal_size()[0] # This gets the size of the current active window of the terminal
WIDTH -= 1
STREAM_CHARS = ['0', '1']
DENSITY = 0.02
MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
time.sleep(2)
print('Press Ctrl-C to exit.')

try:
    channels = [0] * WIDTH 
    # Different results are gotten when
    # channels = [0] * WIDTH is placed inside the while loop.
    while True:
        for i in range(WIDTH):
            if channels[i] == 0 and random.random() <= DENSITY:
                channels[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
            if channels[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                channels[i] -= 1
            else:
                print(' ', end='')
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)
except KeyboardInterrupt:
    print('Digital Stream')
    print('Thanks')
    sys.exit()

    