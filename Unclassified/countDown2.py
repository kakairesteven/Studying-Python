import sevseg, time, sys
secondsLeft = 30.5

try:
    while True:
        print('\n' * 50)
        hour = secondsLeft // 3600
        minutes = (secondsLeft % 3600) // 60
        seconds = (secondsLeft % 60)

        hDigits = str(sevseg.getSevSegStr(hour, 2))
        mDigits = str(sevseg.getSevSegStr(minutes, 2))
        sDigits = str(sevseg.getSevSegStr(seconds, 2))

        hTopRow, hMiddleRow, hBottowRow = hDigits.splitlines()
        mTopRow, mMiddleRow, mBottowRow = mDigits.splitlines()
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        print(hTopRow + '   '+ mTopRow + '   ' + sTopRow)
        print(hMiddleRow, '* ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottowRow + ' * ' + mBottowRow + ' * ' + sBottomRow)
        
        if secondsLeft == 0:
            print()
            print('***BOOM***')
            break

        print()
        print('Press Ctrl-C to quit')
        time.sleep(1)
        secondsLeft -= 1
except KeyboardInterrupt:
    print('CountDown')
    sys.exist()