import random

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])

class guessingGame:

    gametypeDict = {'HARD': 50, 'MEDIUM': 20, 'EASY': 10}

    def __init__(self):
        self.lowerBound = 0
        self.upperBound = 0
        self.secretNumber = 0
        self.difficulty = ''
        self.guesses = 0

    def start(self):
        while True:
            gametype = str.upper(input("""Welcome to Number Guessing Game! If you would like to leave at any time, type 'Exit' 
            
What game type would you like? 
            
Type "EASY", "MEDIUM", or "HARD": """))

            if gametype in self.gametypeDict:
                self.initializeGame(gametype)
                break
            else:
                print('Sorry, but that was not a valid game type, please try again. ')

    def checkExit(self, guess):
        # if input is "exit", end game.
        if guess == 'EXIT':
            print('Thank you for playing. Goodbye!')
            return True
        else:
            return False

    def initializeGame(self, difficulty):
        self.setDifficulty(difficulty)
        self.setSecretNumber()
        return self.startGuessing()

    def startGuessing(self):
        while True:
            self.guesses += 1
            # get input from user
            print('Please guess a number between {} and {}.'.format(self.lowerBound, self.upperBound))

            guess = str.upper(input('Your {} guess: '.format(ordinal(self.guesses))))
            if self.checkExit(guess) is True:
                break
            try:
                guess = int(guess)
            except ValueError:
                print('Input must be integer!')
                continue

            if self.validateInput(guess) == False:
                print('You should provide a number between {} and {}: '.format(format(self.lowerBound, self.upperBound)))
                continue

            # determine if the guess is too low, too high or exactly right
            difference = guess - self.secretNumber

            if difference > 0:
                print('Your guess is too high')
            elif difference < 0:
                print('Your guess is too low')
            else:
                return print('You guessed it! \nYou only needed {} tries to guess the right number.'.format(self.guesses))

    def validateInput(self, number):
        if number > self.lowerBound or number < self.upperBound:
            return True
        else:
            return False

    def setDifficulty(self, difficulty):
        self.difficulty = difficulty
        self.upperBound = self.gametypeDict.get(difficulty)

    def setSecretNumber(self):
        self.secretNumber = random.randint(self.lowerBound, self.upperBound)

def go():
    newGame = guessingGame()
    newGame.start()
