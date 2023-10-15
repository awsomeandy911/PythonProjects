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

# Computer player class built from inheritance from Player
class RandomComputerPlayer(Player):
    # initialize super class
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        # get a random valid spot for users next move
        square = random.choice(game.availableMoves())
        return square

# Human player class built from inheritance from Player
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter + "\'s turn. Input move (0-9):")
            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                validSquare = True # if sucessful then good
            except ValueError:
                print("Invalid square. Try Again!")