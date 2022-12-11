from random import randint
import datetime
from re import M

def getBirthdays(numberOfBirthdays):
    # Starting date
    # Random dates
    # Return list of birthdays
    birthdays = []
    startingDate = datetime.date(2022, 1, 1)
    for i in range(numberOfBirthdays):
        randomDates = datetime.timedelta(randint(0, 364))
        birthday = startingDate + randomDates
        birthdays.append(birthday)
    
    # Understandable birthdays: month, day
    MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    birthdates = []
    for birthday in birthdays:
        monthName = MONTHS[birthday.month - 1]
        day = birthday.day
        birthdates.append('{} {}'.format(monthName, day))
        '''if birthdays.index(birthday) != 0:
        print('{} {}'.format(monthName, day), end=', ')
        '''     
    return birthdates

    
def getMatch(birthDates):
    if len(birthDates) == len(set(birthDates)):
        return None
    matchDates = []
    for a, birthDateA in enumerate(birthDates):
        for b, birthDateB in enumerate(birthDates[a+1:]):
            if birthDateA == birthDateB:
                matchDates.append(birthDateA)
    if len(matchDates) != 0:
        return matchDates
    else:
        return None

while True: # Repeat iteration until the user input is valid.
    numberOfBirthdays = input('Enter number of births: ')
    if numberOfBirthdays.isdecimal() and (0 < int(numberOfBirthdays) <= 100):
        numberOfBirthdays = int(numberOfBirthdays)
        break # Break loop if the response is valid.
birthdays = getBirthdays(numberOfBirthdays)
# print(birthdays)
matchDates = getMatch(birthdays)


if type(matchDates) == list and len(matchDates) > 0:
    print('In a population of {}, there could be {} matching birthdates'.format(numberOfBirthdays, len(matchDates)))
    for i in range(len(matchDates)):
        if i != len(matchDates) - 1:
            print(matchDates[i], end=', ')
        else:
            print(matchDates[i])
else:
    print('In a population of {}, there are no matching birthdates.'.format(numberOfBirthdays))


# Monte Carlo simulation
# Generate 100_000 simulations of birthdays
# Count simulations with matching date births
# Find probability of matching birthdays.

simNumber = 0
for i in range(100_000):
    birthDates = getBirthdays(numberOfBirthdays)
    if i % 1_000 == 0:
        print('Running simulation {} ...'.format(i))
    if getMatch(birthDates) != None:
        simNumber += 1

matchProb = (simNumber/100_000) * 100
print("In a population of {}, there is a {} % probability of the population having matching birthdays.".format(numberOfBirthdays, matchProb))
