'''
    TODO]
        show_map(): map border, time checker, show selectd mode
        display: align center -> showmap, select mode, retry, logo...
'''

import curses
import random, time

'''
    init()
    - desc: Initiating Settings
    - arg: None,
    - return: win    
'''
def init():
    win = curses.initscr()

    curses.noecho()
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.curs_set(2)

    win.keypad(True)

    return win

'''
    landing()
    - desc: Landing Display, Selecting Mode
    - arg: win,
    - return: matrix_size    
'''
def landing(win):
    win.clear()

    win.bkgd(' ', curses.color_pair(1))

    win_y, win_x = win.getmaxyx() 

    win.addstr(3, int(win_x / 2) - 39, str(':::    :::    :::::::::     '), curses.color_pair(1))
    win.addstr(str('::::    ::::   :::::::::::  ::::    :::  :::::::::: '), curses.color_pair(2))
    win.addstr(4, int(win_x / 2) - 39, str(':+:    :+:    :+:    :+:    '), curses.color_pair(1))
    win.addstr(str('+:+:+: :+:+:+      :+:      :+:+:   :+:  :+:        '), curses.color_pair(2))
    win.addstr(5, int(win_x / 2) - 39, str('+:+    +:+    +:+    +:+    '), curses.color_pair(1))
    win.addstr(str('+:+ +:+:+ +:+      +:+      :+:+:+  +:+  +:+        '), curses.color_pair(2))
    win.addstr(6, int(win_x / 2) - 39, str('+#+    +:+    +#++:++#:     '), curses.color_pair(1))
    win.addstr(str('+#+  +:+  +#+      +#+      +#+ +:+ +#+  +#++:++#   '), curses.color_pair(2))
    win.addstr(7, int(win_x / 2) - 39, str('+#+    +#+    +#+    +#+    '), curses.color_pair(1))
    win.addstr(str('+#+       +#+      +#+      +#+  +#+#+#  +#+        '), curses.color_pair(2))
    win.addstr(8, int(win_x / 2) - 39, str('#+#    #+#    #+#    #+#    '), curses.color_pair(1))
    win.addstr(str('#+#       #+#      #+#      #+#   #+#+#  #+#        '), curses.color_pair(2))
    win.addstr(9, int(win_x / 2) - 39, str(' ########     ###    ###    '), curses.color_pair(1))
    win.addstr(str('###       ###  ###########  ###    ####  ########## '), curses.color_pair(2))
    
    win.addstr(int(win_y - 7), int(win_x / 2) - 8, str('-- Choose Mode --'), curses.color_pair(1))
    win.addstr(int(win_y - 5), int(win_x / 2) - 4, str('1. easy '), curses.color_pair(2))
    win.addstr(int(win_y - 4), int(win_x / 2) - 4, str('2. normal '), curses.color_pair(2))
    win.addstr(int(win_y - 3), int(win_x / 2) - 4, str('3. hard '), curses.color_pair(2))

    win.addstr(int(win_y - 2), int(win_x) - 15, str('made@KIMAKUMA'), curses.color_pair(1))

    win.box()

    '''
        Choose Mode
    '''
    win.move(int(win_y) - 5, int(win_x / 2) - 4)

    while(1):
        curs_y, curs_x = win.getyx()
        input = win.getch()

        # up
        if (curs_y > win_y - 5) and (input == 119 or input == 259):
            win.move(int(curs_y) - 1, int(curs_x))

        # down
        elif (curs_y < win_y - 3) and (input == 115 or input == 258):
            win.move(int(curs_y) + 1, int(curs_x))

        # enter
        elif input == 10:
            break

    curs_y, curs_x = curses.getsyx()

    if curs_y == win_y - 5:
        matrix_size = 5

    elif curs_y == win_y - 4:
        matrix_size = 10

    elif curs_y == win_y - 3:
        matrix_size = 20

    return matrix_size

'''
    make_map()
    - desc: Making Minesweeper Map for Answer
    - arg: matrix_size
    - return: matrix
'''
def make_map(matrix_size):
    emo = ['*', '.']
    matrix = []

    for i in range(matrix_size):
        line = []
        
        for j in range(matrix_size):
            # choice로 지뢰 비율 낮춤 <- rand_int = random.randint(0,1)
            rand_int = random.choices(range(0, 2), weights = [0.4, 0.6])
            rand_emo = emo[rand_int[0]]
            line.append(rand_emo)
        matrix.append(line)

    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix[i][j] == '*':
                continue
                
            else:
                matrix[i][j] = 0
                
                for y in range(i - 1, i + 2):
                    for x in range(j -1, j + 2):
                        if y < 0 or x < 0 or y >= matrix_size or x >= matrix_size:
                            continue
                            
                        elif matrix[y][x] == '*':
                            matrix[i][j] += 1
                            
    return matrix

'''
    make_map_q()
    - desc: Making Minesweeper Map for Player
    - arg: matrix_size
    - return: matrix_q
'''
def make_map_q(matrix_size):
    matrix_q = []

    for i in range(matrix_size):
        list_q = []
        
        for j in range(matrix_size):
            list_q.append('-')
            
        matrix_q.append(list_q)

    return matrix_q

'''
    show_map()
    - desc: Show Map, Choose Shell
    - arg: win, matrix_size, matrix_q, cur_x, cur_y
    - return: col, row, cur_x, cur_y
'''
def show_map(win, matrix_size, matrix_q, cur_x, cur_y):
    win.clear()

    win.bkgd(' ', curses.color_pair(1))

    win_y, win_x = win.getmaxyx() 
    start_y = int((win_y / 2) - ((matrix_size + (matrix_size - 1)) / 2))
    start_x = int((win_x / 2) - ((matrix_size + (matrix_size - 1))))

    for i in range(matrix_size):
        for j in range(matrix_size):
            win.addstr(int(start_y + (i * 2)), int(start_x + (j * 4)) , str(matrix_q[i][j]), curses.color_pair(1))

            if j != matrix_size - 1:
                win.addstr(str(' | '), curses.color_pair(1))

        win.addstr(int(start_y + (i * 2) + 1), int(start_x) , str('-' * (matrix_size * 4 - 3)), curses.color_pair(1))

    win.addstr(int(win_y - 2), int(win_x) - 15, str('made@KIMAKUMA'), curses.color_pair(1))

    win.box()

    # cursor moving
    if cur_x == None and cur_y == None: # Game 1st -ing
        win.move(int(start_y), int(start_x)) 
    else: # Game -ing
        win.move(int(cur_y), int(cur_x))

    while(1):
        curs_y, curs_x = win.getyx()
        input = win.getch()

        # up
        if (curs_y > start_y) and (input == 119 or input == 259):
            win.move(int(curs_y - 2), int(curs_x))

        # down
        elif (curs_y < start_y + (matrix_size * 2) - 2) and (input == 115 or input == 258):
            win.move(int(curs_y + 2), int(curs_x))

        # left
        if (curs_x > start_x) and (input == 97 or input == 260):
            win.move(int(curs_y), int(curs_x - 4))

        # right
        elif (curs_x < start_x + (matrix_size * 4) - 4) and (input == 100 or input == 261):
            win.move(int(curs_y), int(curs_x + 4))

        # enter
        elif input == 10:
            break

    curs_y, curs_x = curses.getsyx()

    col = int((curs_x - start_x) / 4)
    row = int((curs_y - start_y) / 2)

    return col, row, curs_x, curs_y

'''
    init_game()
    - desc: Make Map for Game
    - arg: win
    - return: matrix_size, matrix, matrix_q
'''
def init_game(win):
    matrix_size = landing(win)
    matrix = make_map(matrix_size)
    matrix_q = make_map_q(matrix_size)

    return matrix_size, matrix, matrix_q

'''
    confirm()
    - desc: Check Number of Mines, Notice Result of Game
    - arg: matrix_size, matrix, matrix_q
    - return: matrix_cnt, matrix_q_cnt
'''
def confirm(matrix_size, matrix, matrix_q):
    matrix_cnt = 0
    matrix_q_cnt = 0

    for i in range(matrix_size):
        matrix_cnt += matrix[i].count('*')
        matrix_q_cnt += matrix_q[i].count('-')
    
    return matrix_cnt, matrix_q_cnt

'''
    game()
    - desc: Play the MineSweeper, Return Checksum og Game
    - arg: win, matrix_size, matrix, matrix_q, cur_x, cur_y
    - return: checksum, matrix_q, cur_x, cur_y 
'''
def game(win, matrix_size, matrix, matrix_q, cur_x, cur_y):
    matrix_cnt, matrix_q_cnt = confirm(matrix_size, matrix, matrix_q)
    
    # Game Clear
    if matrix_cnt == matrix_q_cnt:
        checksum = 1

    # Show Map()
    col, row, cur_x, cur_y = show_map(win, matrix_size, matrix_q, cur_x, cur_y)
    
    # Game Over
    if matrix[row][col] == '*':
        checksum = 0

    # Game -ing    
    else:
        checksum = -1
        matrix_q[row][col] = matrix[row][col]

    return checksum, matrix_q, cur_x, cur_y

'''
    show_answer()
    - desc: Show Answer Map
    - arg: win, matrix_size, matrix
    - return: None
'''
def show_answer(win, matrix_size, matrix):
    win_y, win_x = win.getmaxyx() 
    start_y = int((win_y / 2) - ((matrix_size + (matrix_size - 1)) / 2))
    start_x = int((win_x / 2) - ((matrix_size + (matrix_size - 1))))

    for i in range(matrix_size):
        for j in range(matrix_size):
            win.addstr(int(start_y + (i * 2)), int(start_x + (j * 4)) , str(matrix[i][j]), curses.color_pair(1))

            if j != matrix_size - 1:
                win.addstr(str(' | '), curses.color_pair(1))

        win.addstr(int(start_y + (i * 2) + 1), int(start_x) , str('-' * (matrix_size * 4 - 3)), curses.color_pair(1))

'''
    gameResult()
    - desc: When Game is Done
    - arg: win, matrix_size, matrix, result
    - return: replay
'''
def gameResult(win, matrix_size, matrix, result):
    win.clear()

    win.bkgd(' ', curses.color_pair(1))

    win_y, win_x = win.getmaxyx()

    if result == 1:
        start_x = int((win_x / 2) - 40)

        win.addstr(3, start_x, str(' _______  _______  _______  _______   ______  _____    _______  _______  ______ \n'), curses.color_pair(1))
        win.addstr(4, start_x, str('|     __||   _   ||   |   ||    ___| |      ||     |_ |    ___||   _   ||   __ \ \n'), curses.color_pair(1))
        win.addstr(5, start_x, str('|    |  ||       ||       ||    ___| |   ---||       ||    ___||       ||      < \n'), curses.color_pair(1))
        win.addstr(6, start_x, str('|_______||___|___||__|_|__||_______| |______||_______||_______||___|___||___|__| \n'), curses.color_pair(1))

    elif result == 0:
        start_x = int((win_x / 2) - 35)

        win.addstr(3, start_x, str(' _______  _______  _______  _______   _______  ___ ___  _______  ______  \n'), curses.color_pair(1))
        win.addstr(4, start_x, str('|     __||   _   ||   |   ||    ___| |       ||   |   ||    ___||   __ \ \n'), curses.color_pair(1))
        win.addstr(5, start_x, str('|    |  ||       ||       ||    ___| |   -   ||   |   ||    ___||      < \n'), curses.color_pair(1))
        win.addstr(6, start_x, str('|_______||___|___||__|_|__||_______| |_______| \_____/ |_______||___|__| \n'), curses.color_pair(1))

    show_answer(win, matrix_size, matrix)

    win.addstr(int(win_y - 7), int(win_x / 2) - 4, str('-- RETRY --'), curses.color_pair(1))
    win.addstr(int(win_y - 5), int(win_x / 2) - 2, str('1. YES '), curses.color_pair(2))
    win.addstr(int(win_y - 4), int(win_x / 2) - 2, str('2. NO '), curses.color_pair(2))

    win.addstr(int(win_y - 2), int(win_x) - 15, str('made@KIMAKUMA'), curses.color_pair(1))

    win.box()

    '''
        Choose Mode
    '''
    win.move(int(win_y) - 5, int(win_x / 2) - 2)

    while(1):
        curs_y, curs_x = win.getyx()
        input = win.getch()

        # up
        if (curs_y > win_y - 5) and (input == 119 or input == 259):
            win.move(int(curs_y) - 1, int(curs_x))

        # down
        elif (curs_y < win_y - 4) and (input == 115 or input == 258):
            win.move(int(curs_y) + 1, int(curs_x))

        # enter
        elif input == 10:
            break

    curs_y, curs_x = curses.getsyx()

    if curs_y == win_y - 5:
        replay = 1

    elif curs_y == win_y - 4:
        replay = 0

    return replay

