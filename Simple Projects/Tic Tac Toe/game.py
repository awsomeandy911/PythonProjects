class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # use single list to represnt 3x3 tic tac toe board
        self.currentWinner = None # keeps track of winner

    def printBoard(self):
        # to get rows for game
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
