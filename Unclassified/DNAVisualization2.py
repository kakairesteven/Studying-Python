import random, sys, time
PAUSE = 0.15
ROWS = [
    #123456789 <- Use this to measure the number of spaces:
    '         ##', # Index 0 has no {}.
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '     #{}------{}#',
    '     #{}-----{}#',
    '      #{}---{}#',
    '       #{}-{}#',
    '        ##',
    '       #{}-{}#',
    '      #{}---{}#',
    '     #{}-----{}#',
    '     #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#'
]

print('DNA visualization')
rowIndex = 0
time.sleep(2) # pause for 2 seconds, sleep time must be non-negative.

try:
    while True:
        rowIndex += 1 # Increment rowIndex to get the next row.
        if rowIndex == len(ROWS):
            rowIndex = 0
        ranndomSelection = random.randint(1, 4)
        if ranndomSelection == 1:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif ranndomSelection == 2:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif ranndomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif ranndomSelection == 4:
            leftNucleotide, rightNucleotide = 'G', 'C'
        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(PAUSE) # sleep time must be non-negative.
except KeyboardInterrupt:
    sys.exit()