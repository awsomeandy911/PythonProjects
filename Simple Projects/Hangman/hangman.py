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
    # what user has guessed
    usedLetters = set()