

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

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerXMove == '2':
        pos2 = 'X'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerXMove == '3':
        pos3 = 'X'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerXMove == '4':
        pos4 = 'X'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerXMove == '5':
        pos5 = 'X'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerXMove == '6':
        pos6 = 'X'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerXMove == '7':
        pos7 = 'X'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerXMove == '8':
        pos8 = 'X'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerXMove == '9':
        pos9 = 'X'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')


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

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerOMove == '2':
        pos2 = 'O'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerOMove == '3':
        pos3 = 'O'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerOMove == '4':
        pos4 = 'O'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerOMove == '5':
        pos5 = 'O'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerOMove == '6':
        pos6 = 'O'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerOMove == '7':
        pos7 = 'O'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerOMove == '8':
        pos8 = 'O'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')

    if playerOMove == '9':
        pos9 = 'O'

        print('--------')
        print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
        print('--------')


def board():

    print('--------')
    print(' '+ pos7 +'|'+ pos8 +'|'+ pos9 +'   ')
    print('--------')
    print(' '+ pos4 +'|'+ pos5 +'|'+ pos6 +'   ')
    print('--------')
    print(' '+ pos1 +'|'+ pos2 +'|'+ pos3 +'   ')
    print('--------')

while not gameExit:

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
