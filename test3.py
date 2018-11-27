import random
pos1 = ' '  ; pos2 = ' ' ; pos3 = ' ' ; pos4 = ' ' ; pos5 = ' ' ; pos6 = ' ' ; pos7 = ' ' ; pos8 = ' ' ; pos9 = ' '
gameExit = False
userTurn = 0
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

def board():

    print('--------')
    print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
    print('--------')
    print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
    print('--------')
    print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
    print('--------')

def usr_Input():

    global userTurn

    while userTurn < 9:


       # turn 1 - player 1
       usrInput = input('choose move 1-9: ') 
       if userTurn == 1:
           pos1 = player1
           board()

def vaild_moves():
    
    print(1)


while not gameExit:

    game_start_menu()
    who_goes_first()
    vaild_moves()
    usr_Input()
    board()