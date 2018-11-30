import random
import time

longTime = 1
shortTime = 0.5

def game_start_menu():

    print('________Tic Tac Toe________')
    # time.sleep(shortTime)
    print('Now rolling to choose player....')
    time.sleep(shortTime)
    print('....')
    time.sleep(shortTime)
    print('....')
    time.sleep(shortTime)
    print('....')
    # time.sleep(shortTime)
    randomToChoosePlayer = random.randint(0,1)
    print('rolled')
    print(randomToChoosePlayer)
    #print(randomToChoosePlayer) # used to check roll outcome
    time.sleep(longTime)
    # time.sleep(longTime)



    if randomToChoosePlayer == 0:
        print('player 1 is X, player 2 is O')
        print('X goes first, player 1 please select move. ')
        time.sleep(longTime)
    elif randomToChoosePlayer == 1:
        print('player 2 is X, player 1 is O')
        print('X goes first, player 2 please select move. ')
        time.sleep(longTime)


def instruction_board():

    print('--BOARD-INSTRUCTIONS--')
    print('--------')
    print(' 7|8|9  ')
    print('--------')
    print(' 4|5|6  ')
    print('--------')
    print(' 1|2|3  ')
    print('--------')
