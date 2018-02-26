import random

class game:
    def __init__(self, lower, upper, difficulty, randomNum):
        self.lower = lower
        self.upper = upper
        self.difficulty = difficulty
        self.randomNum = randomNum


def getRandNum(lowerNum, upperNum):
   return random.randint(lowerNum, upperNum)


def startNewGame():
    gametypeDict = {'HARD': 50, 'MEDIUM': 20, 'EASY': 10}
    numGuesses = 1

    while True:
        gametype = str.upper(input('What game type would you like? Type "easy", "medium", or "hard"'))
        newGame = game(0, 0, 'easy', 0)

        if gametype in gametypeDict:
            newGame.upper = gametypeDict.get(gametype)
            newGame.difficulty = gametype
            newGame.randomNum = getRandNum(0, gametypeDict.get(gametype))
            print('You have selected {}. Therefore, you will need to guess a number between {} and {}'.format(newGame.difficulty, newGame.lower, newGame.upper))
            break
        else:
            print('Sorry, but that was not a valid game type, please try again')

    guess = getGuess(newGame.upper, newGame.lower)
    while evalFunc(guess, newGame.randomNum) != 0:
        if evalFunc(guess, newGame.randomNum) == 2:
            print('Too high!')
            numGuesses += 1
            guess = getGuess(newGame.upper, newGame.lower)
        else:
            print('Too low!')
            numGuesses += 1
            guess = getGuess(newGame.upper, newGame.lower)

    if numGuesses == 1:
        trytext = 'try'
    else:
        trytext = 'tries'
    print('You guessed ', str(guess), 'and you were correct! It took you', str(numGuesses), trytext)


def evalFunc(checkNum, realNum):
    if checkNum == realNum:
        return int(0)
    elif checkNum < realNum:
        return int(1)
    else:
        return int(2)

#getGuess function will retrieve a new guess from the user as int. It also handles exceptions.
def getGuess(upper, lower):
    upper = upper
    lower = lower
    guess = 0

    while True:
        try:
            guess = int(input('Please guess a number between {} and {}:'.format(lower, upper)))
        except ValueError:
            print('You may only input whole numbers. Please try again.')
            continue
        if guess > (lower - 1) and guess < (upper + 1):
            return int(guess)
        else:
            print('Your last guess was outside of the range. Please enter a guess between and including {} and {}'.format(lower, upper))


startNewGame()


        # if type(guess) != int:
        #     print('You may only input whole numbers. Please try again.')
        # elif guess > (lower - 1) and guess < (upper  + 1):
        #     return int(guess)
        # else:
        #     print('Your last guess was outside of the range. Please enter a guess between and including {} and {}'.format(lower, upper))








# def playGame(guessrange):
#     guess = getGuess()
#     magicNum = guessrange
#     numGuesses = 0
#     while evalFunc(guess, magicNum) != 0:
#         if evalFunc(guess, magicNum) == 2:
#             print('Too high!')
#             guess = getGuess()
#             numGuesses += 1
#         else:
#             print('Too low!')
#             guess = getGuess()
#             numGuesses += 1
#
#     print('You guessed ', str(guess), 'and you were correct!')


# def startNewGame1():
#     gametypeDict = {'HARD': 50, 'MEDIUM': 20, 'EASY': 10}
#
#     print("We're starting a new game. Let's get started!")
#
#     while True:
#         gametype = str.upper(input('What game type would you like? Type "easy", "medium", or "hard"'))
#         if gametype in gametypeDict:
#
#             newGame = game(0,gametypeDict.get(gametype), gametype, getRandNum(0, gametypeDict.get(gametype)))
#             return newGame
#         else:
#             print('Sorry, but that was not a valid game type, please try again')

# def getRandNum(lowerNum, upperNum):
#    return random.randint(lowerNum, upperNum)

    #gametypeDict.get(gametype, 'sorry that was not a valid game type. Please try again')

#
# a = 'this'
# print('%a is a test' %(a))

# guess = int(input('guess a num: '))
#
# guesscheck = evalFunc(guess, magicNum)
#
# while guesscheck != 0:
#     if guesscheck == 1:
#         guess = int(input('guess higher number: '))
#     elif guesscheck == 2:
#         guess = int(input('guess lower number: '))
#     guesscheck = evalFunc(guess, magicNum)


