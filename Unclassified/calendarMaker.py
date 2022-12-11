import datetime
# Prompt user to enter year and month.
# Display Calendar for the given month in a given year.
# Save file


# Constants: weekSeparators, blankRows
# Variables: calText, dateLabel
MONTHS = ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')

weekdayText = '....Sunday....Monday......Tuesday.....Wednesday....Thursday....Friday.....Saturday';
weekSeparator = '+-----------' * 7 + '+\n'
blankRow = '|           ' * 7 + '|\n'

# Prompt user to enter year
while True: # Prompt user to enter correct year and month:
    year = input("Enter the calendar year, e.g 2022: ")
    # print(year)

    month = input("Enter the calendar month, i.e 1-12: ")
    # print(month)
    if year.isdecimal() and len(year) == 4 and month.isdecimal() and 1 <= int(month) <= 12:
        year = int(year)
        month = int(month)
        break
    else:
        print('Invalid month or year entered: Please try again.')


def getCalendar(year, month):
    calText = ''
    calText += ' ' * 35 + str(MONTHS[month - 1]) + ' ' + str(year) + '\n'
    calText += weekdayText +' \n'
    currentDate = datetime.datetime(year, month, day=1)
    # print('Current Day: {}/{}.'.format(currentDate.year, currentDate.month))
    # print(currentDate.weekday())

    # Roll back date until weekday is a Sunday
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)
    
    while True: 
        calText += weekSeparator
        for i in range(7):
            if currentDate.month == month:
                dateLabel = currentDate
                calText += '|' + str(dateLabel.day).rjust(2) + ' ' + ' ' * 8
                currentDate += datetime.timedelta(days=1)
            else:
                dateLabel = ''
                calText += '|' + dateLabel.rjust(2) + ' ' + ' ' * 8
                currentDate += datetime.timedelta(days=1)
        
            
        calText += '|\n'

        for i in range(3):
            calText += blankRow
        
        
        if currentDate.month != month:
            break
    calText += weekSeparator
    return calText

calText = getCalendar(year, month)
print(calText)

# Save file
calendarFile = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFile, 'w') as fileObj:
    fileObj.write(calText)

print('Calendar saved to', calendarFile)
