

def board():

    print('--------')
    print(' '+ pos7 +'| '+ pos8 +'|'+ pos9 +'   ')
    print('--------')
    print(' '+ pos4 +'| '+ pos5 +'|'+ pos6 +'   ')
    print('--------')
    print(' '+ pos1 +'| '+ pos2 +'|'+ pos3 +'   ')
    print('--------')


def player_X_options():

    playerXMove = input('choose 1-9 to move: ')


    if playerXMove == '1':
        pos1 = 'X'

        print('--------')
        print(' '+ pos7 +'| '+ pos8 +'|'+ pos9 +'   ')
        print('--------')
        print(' '+ pos4 +'| '+ pos5 +'|'+ pos6 +'   ')
        print('--------')
        print(' '+ pos1 +'| '+ pos2 +'|'+ pos3 +'   ')
        print('--------')


pos1 = ' '
pos2 = ' '
pos3 = ' '
pos4 = ' '
pos5 = ' '
pos6 = ' '
pos7 = ' '
pos8 = ' '
pos9 = ' '


board()
player_X_options()
