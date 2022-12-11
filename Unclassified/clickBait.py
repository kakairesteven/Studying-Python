import random

# Set up the constants:
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESSIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['Iganga', 'Kampala', 'Jinja', 'Gulu', 'London', 'New York',
'Boston', 'Texas', 'Georgia', 'North Carolina', 'Michigan']

NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avacado',
'Plastic straw', 'Serial Killer', 'Telephone Psychic']

PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
'Workplace', 'Donut Shop', 'Apocalypse Bunker' ]

WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next week']


def main():
    print('Clickbait Headline Generator')
    print('By Kakaire Steven')

    print()

    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            numberOfHeadlines = int(response)
            break # Exit the loop once a valid number is entered.


    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1, 8)

        if clickbaitType == 1:
            headline = generateAreMillennialsKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadline()
        elif clickbaitType == 7:
            headline = generateReasonsWhyHeadline()

        print(headline)
    print()

    website = random.choice(['Wobsite', 'blag', 'Facebuuk', 'Googles',
    'Facesbook', 'Tweedie', 'Pastagram'])
    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, 'or you\'re fired!')

# Each of these functions returns a different type of headline:
def generateAreMillennialsKillingHeadline():
    noun = random.choice(NOUNS)
    return '''
    Are Millenials killing the {} Industry
    '''.format(noun)

def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS)
    when = random.choice(NOUNS) + 's'
    return '''Without This {},
        {} Could kill you {}
        '''.format(noun, pluralNoun, when)

def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return '''Big Companies Hate {}! See How This
        {} {} Invented a Cheaper {}
        '''.format(pronoun, state, noun1, noun2)

def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice( NOUNS)
    pronoun = random.choice(POSSESSIVE_PRONOUNS)
    place = random.choice(PLACES)
    return '''
        You Won\'t Believe This
        {} {} Found in {} {}
        '''.format(state, noun, pronoun, place)

def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return '''
    {} Gift Ideas to Give
        your {} from {}'''.format(number, noun, state)

def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return '''
        What {} Don\'t want you to know
        about {}
        '''.format(pluralNoun1, pluralNoun2)

def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    # number2 should be no longer than number1:
    number2 = random.randint(1, number1)
    return '''
        {} Reasons why {} are more interesting
        than you think
        (Number {} will suprise you!)
        '''.format(number1, pluralNoun, number2)

def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESSIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS
    if pronoun1 == 'Their':
        return '''
        This {} {} Didn\'t Think Robots
        Would Take {} Job. {} Were Wrong
        '''.format(state, noun, pronoun1, pronoun2)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()