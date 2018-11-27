import time

pos1 = ' '
pos2 = ' '
pos3 = ' '
pos4 = ' '
pos5 = ' '
pos6 = ' '
pos7 = ' '
pos8 = ' '
pos9 = ' '

gameExit = False

def player_X_options():

    global pos1
    global pos2
    global pos3
    global pos4
    global pos5
    global pos6
    global pos7
    global pos8
    global pos9

    playerXMove = input('choose 1-9 to move: ')


    if playerXMove == '1':
        pos1 = 'X'
        board()

    elif playerXMove == '2':
        pos2 = 'X'
        board()

    elif playerXMove == '3':
        pos3 = 'X'
        board()

    elif playerXMove == '4':
        pos4 = 'X'
        board()

    elif playerXMove == '5':
        pos5 = 'X'
        board()

    elif playerXMove == '6':
        pos6 = 'X'
        board()

    elif playerXMove == '7':
        pos7 = 'X'
        board()
    elif playerXMove == '8':
        pos8 = 'X'
        board()

    elif playerXMove == '9':
        pos9 = 'X'
        board()


def player_O_options():

    global pos1
    global pos2
    global pos3
    global pos4
    global pos5
    global pos6
    global pos7
    global pos8
    global pos9

    playerOMove = input('choose 1-9 to move: ')


    if playerOMove == '1':
        pos1 = 'O'
        board()

    elif playerOMove == '2':
        pos2 = 'O'
        board()

    elif playerOMove == '3':
        pos3 = 'O' 
        board()

    elif playerOMove == '4':
        pos4 = 'O'
        board()

    elif playerOMove == '5':
        pos5 = 'O'
        board()

    elif playerOMove == '6':
        pos6 = 'O'
        board()

    elif playerOMove == '7':
        pos7 = 'O'
        board()

    elif playerOMove == '8':
        pos8 = 'O'
        board()

    elif playerOMove == '9':
        pos9 = 'O'
        board()


def board():

    print('--------')
    print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
    print('--------')
    print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
    print('--------')
    print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
    print('--------')

def valid_moves():
    if pos1 == 'X' or pos1 == 'O':
        print('invalid move')

    elif pos2 == 'X' or pos2 == 'O':
        print('invalid move')  
    
    elif pos3 == 'X' or pos3 == 'O':
        print('invalid move')   

    elif pos4 == 'X' or pos4 == 'O':
        print('invalid move')  

    elif pos5 == 'X' or pos5 == 'O':
        print('invalid move')  

    elif pos6 == 'X' or pos6 == 'O':
        print('invalid move')
    
    elif pos7 == 'X' or pos7 == 'O':
        print('invalid move')   

    elif pos8 == 'X' or pos8 == 'O':
        print('invalid move')   

    elif pos9 == 'X' or pos9 == 'O':
        print('invalid move')   



while not gameExit:
    
    valid_moves()
    player_X_options()
    player_O_options()
    



# notes

# what does return do in python?

# e.g:
# def getPlayerMove(board):
    # Let the player type in his move.
    #move = ' '
    #while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
    #    print('What is your next move? (1-9)')
    #    move = input()
#    return int(move)
