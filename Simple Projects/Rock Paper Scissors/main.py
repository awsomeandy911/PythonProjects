import random

# function to play the game
def play():
    print("Welcome to the game of Rock, Paper, Scissors!!!")
    # have user enter rock, paper, or scissors
    user = input("'R' for rock, 'P' for paper, 'S' for scissors").upper() # keeps user input uppercase
    # computer randomly chooses a move
    computer = random.choice(['R', 'P', 'S'])
    if user == computer:
        return f'It\'s a tie! Computer played: {computer}'
    if isWin(user, computer):
        return f'You Won!!! Computer played: {computer} :)'
    
    return f'You lost! Computer played: {computer} :('

# rock > scissors, scissors > paper, paper > rock
def isWin(player, opponent):
    # returns true if player beats opponent 
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') \
        or (player == 'P' and opponent == 'R'):
        return True
    
print(play())