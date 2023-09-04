import random

def guess(x):
    randomNum = random.randint(1, x)
    guess = 0
    while guess != randomNum:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < randomNum:
            print('Too low, guess again')
        elif guess > randomNum:
            print('Too high, guess again')
            
    print(f'Correct! You guessed the right number! {randomNum} Good Job!!!')        

guess(10)