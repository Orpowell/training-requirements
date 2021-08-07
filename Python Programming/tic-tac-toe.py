import random
import re
import sys
import time

board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

# Regular expressions for X winning
x_win_codes = ['XXX......',
               '...XXX...',
               '......XXX',
               'X..X..X..',
               '.X..X..X.',
               '..X..X..X',
               'X...X...X',
               '..X.X.X..']

# Regular expressions for O winning
o_win_codes = ['OOO......',
               '...OOO...',
               '......OOO',
               'O..O..O..',
               '.O..O..O.',
               '..O..O..O',
               'O...O...O',
               '..O.O.O..']

# Regular expression for a drawn board
draw_code = 'X|OX|OX|OX|OX|OX|OX|OX|OX|OX|O'


# Generate the game board
def show_board():
    i = 0
    print("##################")
    print('   ', 0, '  ', 1, '  ', 2)
    for row in board:
        print(i, row)
        i +=1
    print("##################")
    i = 0


# Choose symbol for Game - X starts
def choose_symbol():
    symbol = input("X or O? ")
    if symbol == 'X':
        game_mode = 0
        return game_mode
    elif symbol == 'O':
        game_mode = 1
        return game_mode
    else:
        print('Error: Please choose X or O')
        b = choose_symbol()
        return b


# Collect row coordinate
def get_row():
    row = input('What row?')
    if row not in ['1', '2', '0']:
        print('Invalid: Choose 0, 1, or 2 for row')
        a = get_row()
        return int(a)
    else:
        return int(row)


# Collect column coordinate
def get_column():
    column = input('What column?')
    if column not in ['1', '2', '0']:
        print('Invalid: Choose 0, 1, or 2 for column')
        col = get_column()
        return int(col)
    else:
        return int(column)


# Collect row & column and place player symbol on board
def place_symbol():
    row = get_row()
    column = get_column()
    confirm_coordinate = input(
        'place {symbol} at row {row}, column {column}? [y to confirm, press enter to reselect]'.format(symbol=symbol, row=row, column=column))
    coordinate = board[row][column]
    if confirm_coordinate == 'y' and coordinate == '-':
        board[row][column] = symbol
    else:
        print('Please reselect (Hint: The position you selected may be occupied)')
        place_symbol()
    print('Move placed!')
    show_board()


# Robot places symbol on board
def robot_place_symbol():
    row = random.randint(0, 2)
    column = random.randint(0, 2)
    coordinate = board[row][column]
    if coordinate == '-':
        board[row][column] = robot_symbol
        print(f'Computer placed {robot_symbol} at row {row}, column {column}!')
        show_board()
    else:
        robot_place_symbol()


# Check if player using O symbol has won/drawn
def O_check_win():
    game_code = ''
    i = 0
    for row in board:
        game_code = game_code + ''.join(board[i])
        i += 1

    for win in o_win_codes:
        x = re.search(win, game_code)
        if x is not None:
            print(f'{O_player} Wins!')
            sys.exit()
        y = re.search(draw_code, game_code)
        x = re.search('-', game_code)
        if y is not None and x is None:
            print('Draw!')
            sys.exit()


# Check if player using X symbol has won/drawn
def X_check_win():
    game_code = ''
    i = 0
    for row in board:
        game_code = game_code + ''.join(board[i])
        i += 1

    for win in x_win_codes:
        x = re.search(win, game_code)
        if x is not None:
            print(f'{X_player} Wins!')
            sys.exit()
    y = re.search(draw_code, game_code)
    x = re.search('-', game_code)
    if y is not None and x is None:
        print('Draw!')
        sys.exit()


# Run Game
if __name__ == '__main__':
    game_mode = choose_symbol()
    show_board()

    # If player chooses X symbol
    if game_mode == 1:
        symbol = 'O'
        robot_symbol = 'X'
        X_player = 'Computer'
        O_player = 'Player'
        for r in range(0, 8):
            robot_place_symbol()
            X_check_win()
            time.sleep(1)
            place_symbol()
            O_check_win()

    # If player chooses O symbol
    else:
        symbol = 'X'
        robot_symbol = 'O'
        X_player = 'Player'
        O_player = 'Computer'
        for r in range(0, 8):
            place_symbol()
            X_check_win()
            time.sleep(1)
            robot_place_symbol()
            O_check_win()
