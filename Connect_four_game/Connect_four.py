from collections import deque
import operator
from colorama import Fore


def player_marking_count(r, c, dx, dy, oper):
    counter = 0
    for i in range(1, 4):
        new_row = oper(r, (dx * i))
        new_col = oper(c, (dy * i))

        if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
            break

        if game_board[new_row][new_col] != player_symbol:
            break

        counter += 1
    return counter


def check_for_win(r, c, ):
    for x, y in directions:
        counter = player_marking_count(r, c, x, y, operator.add) + player_marking_count(r, c, x, y, operator.sub) + 1

        if counter >= 4:
            return True

    if total_moves == ROWS * COLS:
        print('Draw! Play one more game.')
        raise SystemExit
    return False


def print_game_board():
    [print(f"[ {', '.join(r)} ]") for r in game_board]


def player_move(player_col):
    current_row = 0
    while current_row != ROWS and game_board[current_row][player_col] == '0':
        current_row += 1

    return current_row - 1


ROWS, COLS = 6, 7
total_moves = 0

game_board = [['0'] * COLS for _ in range(ROWS)]

print_game_board()

player_one = Fore.BLUE + '1' + Fore.RESET
player_two = Fore.GREEN + '2' + Fore.RESET

turns = deque([[1, player_one], [2, player_two]])

win = False

directions = (

    (-1, 0),  # up
    (0, -1),  # left
    (-1, -1),  # up-left
    (-1, 1)  # up-right
)

while not win:
    player_num, player_symbol = turns[0]
    try:
        player_column_choice = int(input(f'Player {player_num} turn. Choose a column:')) - 1
    except ValueError:
        print(Fore.RED + f'Please choose a valid column between 1- {COLS}' + Fore.RESET)
        continue

    if not 0 <= player_column_choice < COLS:
        print(Fore.RED + f'Please choose a valid column between 1- {COLS}' + Fore.RESET)
        continue

    if game_board[0][player_column_choice] != '0':
        print(Fore.RED + 'You cannot put in this column. Please choose another one!' + Fore.RESET)
        continue

    row = player_move(player_column_choice)
    game_board[row][player_column_choice] = player_symbol
    total_moves += 1

    if check_for_win(row, player_column_choice):
        win = True
        break
    print_game_board()
    turns.rotate()

print_game_board()
print(f'Player {turns[0][0]} wins !')
