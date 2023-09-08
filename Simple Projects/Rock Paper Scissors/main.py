import random

# function to play the game
def play():
    print("Welcome to the game of Rock, Paper, Scissors!!!")
    # have user enter rock, paper, or scissors
    user = input("'R' for rock, 'P' for paper, 'S' for scissors"). lower() # keeps user input lowercase
    # computer randomly chooses a move
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return f'It\'s a tie! Computer played {computer}'
    if isWin(user, computer):
        return 'You Won!!!'
    
    return f'You lost! Computer played {computer} :('

# rock > scissors, scissors > paper, paper > rock
def isWin(player, opponent):
    # returns true if player beats opponent 
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    
print(play())