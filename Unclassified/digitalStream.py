import random, shutil, time, sys

# Set up the constants:
MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
STREAM_CHARS = ['0', '1']

# Density can range from 0.0 to 1.0:
DENSITY = 0.02

# Get the size of the terminal window:
WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

print('Digital stream')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if columns[i] == 0 and random.random() <= DENSITY:
                # Restart the stream on this column.
                columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
            # Display an empty space or 1/0 character.
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print() # Print a newline at the end of the row of columns.
        sys.stdout.flush() # Make sure text appears on the screen.
        time.sleep(PAUSE)
           
except KeyboardInterrupt:
    sys.exit()