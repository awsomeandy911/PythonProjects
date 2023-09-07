import random

def guess(x):
    # generates a random num for user to guess
    randomNum = random.randint(1, x)
    # initialize guess variable
    guess = 0
    # while loop until user guesses correct random num
    while guess != randomNum:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < randomNum:
            print('Too low, guess again')
        elif guess > randomNum:
            print('Too high, guess again')
            
    print(f'Correct! You guessed the right number! {randomNum}, Good Job!!!')        

# inverse function of guess where the computer guesses the user's number
def computerGuess(x):
    print("\nLet's play another game! \
          \nPick a number between 1-10. Dont say it out loud!!!")
    # range of numbers the computer can guess
    low = 1
    high = x
    # initialize feedback variable
    feedback = ''
    # while loop until computer guesses correct random num
    while feedback != 'c':
        # checks to make sure low and high are not the same value
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high bc low = high
        # ask user questions to direct computer to guess correctly
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C??)'). lower() # keeps user input lowercase
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
    print(f'Correct! The computer guessed the right number! {guess}, Good Job!!!')

guess(10)
computerGuess(10)