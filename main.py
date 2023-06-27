import curses
import time
import functions

try:
    while(1):
        cur_x, cur_y = None, None
        win = functions.init()

        matrix_size, matrix, matrix_q = functions.init_game(win)

        # Game 1st -ing
        checksum, matrix_q, cur_x, cur_y = functions.game(win, matrix_size, matrix, matrix_q, cur_x = None, cur_y = None)

        while(1):
            checksum, matrix_q, cur_x, cur_y = functions.game(win, matrix_size, matrix, matrix_q, cur_x, cur_y)

            if checksum == 0 or checksum == 1:
                replay = functions.gameResult(win, matrix_size, matrix, checksum)
                break

            else:
                continue

        if replay == 0:
            break

finally:
    curses.endwin()