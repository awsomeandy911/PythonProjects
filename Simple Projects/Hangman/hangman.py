# import random library package and words from words.py
import random
from words import words

def getWord(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = getWord(words)