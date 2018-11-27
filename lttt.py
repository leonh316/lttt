import modules.menu as menu
import modules.board as board
import random

pos1 = ' '  ; pos2 = ' ' ; pos3 = ' ' ; pos4 = ' ' ; pos5 = ' ' ; pos6 = ' ' ; pos7 = ' ' ; pos8 = ' ' ; pos9 = ' '
userTurn = 0
player1 = 'x'
player2 = 'o'
gameExit = False


def usr_Input():

    global userTurn
    global player1

    while userTurn < 9:

       # turn 1 - player 1
       usrInput = input('choose move 1-9: ') 
       if userTurn == 1:
           pos1 = player1
           board.board()

def vaild_moves():
    
    print(1)


while not gameExit:

    menu.game_start_menu()
    menu.who_goes_first()
    vaild_moves()
    usr_Input()
    board.board()


