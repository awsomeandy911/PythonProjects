# import random library package and words from words.py
import random
from words import words
import string

# function to get valid words
def getValidWord(words):
    # randomly chooses something from the list
    word = random.choice(words) 
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper() # keeps user input uppercase

# function to keep track of valid words
def hangman():
    word = getValidWord(words)
    # letters in the word
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    # what letters user has guessed
    guessedLetters = set()

    # tracks amount of lives user has
    lives = 6

    # get user input with these conditions
    while len(wordLetters) > 0 and lives > 0:
        # letters used
        print("You have used these letters:", " ".join(guessedLetters),"and you have", lives, "lives left") #" ".join(['a', 'b', 'c']) --> "a b c"

        # current status of the word i.e (W _ R D)
        worldList = [letter if letter in guessedLetters else '_' for letter in word]
        print("Current word: ", " ".join(worldList))

        userLetter = input("Guess a Letter: ").upper() # keeps input upper case
        if userLetter in alphabet - guessedLetters:
            guessedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives = lives - 1 # takes away 1 life if user guessed wrong
                print("The letter " + userLetter + " is not in the word")
        
        elif userLetter in guessedLetters:
            print("You literally just guessed that letter -_- Try again")
        
        else:
            print("Invalid character, Try again")
    
    if lives == 0:
        print("GG, you lost all your lives. Try Again")
    else:
        print("Yay you guessed the word!: " + word)
    

hangman()