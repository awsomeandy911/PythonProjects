class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # use single list to represnt 3x3 tic tac toe board
        self.currentWinner = None # keeps track of winner

    def printBoard(self):
        # to get rows for game
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def printBoardNumbers():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        numberBoard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print("| " + " | ".join(row) + " |") 

    def availableMoves(self):
        # return []
        moves = []
        for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] the spot of X's and O's
            if spot == ' ':
                moves.append(i)
        return moves
    
    def emptySquares(self):
        return " " in self.board
    
    def numEmptySquares(self):
        return self.bnoard.count(" ")
    
    def makeMove(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true, if invalid, return false
        if self.board[square] == " ":
            self.board[square] = letter
            return True
        else:
            return False
        

def play(game, xPlayer, oPlayer, printGame = True):
    if printGame:
        game.printBoardNumbers()

    letter = "X" # starting letter
    # iterate while the game still has empty squares
    # don't worry about winner bc once found then loop is broken
    while game.emptySquares():
        # get the move from the appropriate player
        if letter == "O":
            square = oPlayer.getMove