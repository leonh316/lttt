# testing how to add to check for vaild and invalid moves

pos1 = ' '
pos2 = ' '
pos3 = ' '
pos4 = ' '
pos5 = ' '
pos6 = ' '
pos7 = ' '
pos8 = ' '
pos9 = ' '

def player_X_move_options():


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
def player_O_move_options():

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
    print('  | |   ')
    print('--------')
    print('  | |   ')
    print('--------')
    print('  | |   ')
    print('--------')


board()
player_X_move_options()
player_O_move_options()



"""
if playerXMove or playerOMove
    check to see if valid move

list of vaild moves
    if box is open and not already taken
list of moves which mean game won,lost,draw


"""