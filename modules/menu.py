import random

player1 = 'x'
player2 = 'o'


def game_start_menu():

    print('________Tic Tac Toe________')
  
    print('Now rolling to choose player....')

def who_goes_first():
    global player1
    global player2

    # players to choose symbol
    chooseSymbol = input('player 1: enter X or O to choose your symbol: ')
    player1 = chooseSymbol
    if player1 == 'x':
        player2 = 'o'
    if player1 == 'x':
        player2 = 'o'
    
    print('player 2 is: ' + player2)
  
    print('random dice roll to choose who goes first')
    print('rolling....')
    randomToChoosePlayer = random.randint(0,1)
    print('rolled')
    print(randomToChoosePlayer)
    if randomToChoosePlayer == 0:
        playerA = player1
        playerB = player2

    if randomToChoosePlayer == 1:
        playerA = player2
        playerB = player1
