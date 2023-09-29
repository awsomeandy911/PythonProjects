import math
import random

# base player class
class Player:
    # initialize player
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    # players need to get their next move given a game
    def getMove(self, game):
        pass