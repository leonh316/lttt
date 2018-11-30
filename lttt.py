import random
import time
import modules.menu as menu
import modules.board as board

# sleep times
longTime = 1
shortTime = 0.5
gameExit = False


# sleep time


menu.game_start_menu()

menu.instruction_board()

while not gameExit:

    board.player_X_move_options()
    board.player_O_move_options()
