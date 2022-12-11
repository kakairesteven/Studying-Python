import time, sevseg, sys

try:
    while True:
        print('\n' * 60)
        # Current time
        currentTime = time.localtime()
        # print(currentTime)

        #Current time hour
        currenthour = currentTime.tm_hour % 12
        if currenthour == '0':
            currenthour = '12'
        currentMinute = currentTime.tm_min
        currentSec = currentTime.tm_sec

        # Sevseg
        hDigits = sevseg.getSevSegStr(str(currenthour), 2)
        mDigits = sevseg.getSevSegStr(str(currentMinute), 2)
        sDigits = sevseg.getSevSegStr(str(currentSec), 2)

        hTop, hMiddle, hLower = hDigits.splitlines()
        mTop, mMiddle, mLower = mDigits.splitlines()
        sTop, sMiddle, sLower = sDigits.splitlines()

        print(hTop + '   ' + mTop + '   ' + sTop)
        print(hMiddle + ' * ' + mMiddle + ' * ' + sMiddle)
        print(hLower + ' * ' + mLower + ' * ' + sLower)
        print()
        print('Press Ctrl-C to quit.')

        while True:
            time.sleep(0.001)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break

except KeyboardInterrupt:
    sys.exit() # When Ctrl-C is pressed, end the program.