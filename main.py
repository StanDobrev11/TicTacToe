from math import floor

from colorama import Fore


def create_board_nums():
    # 1 | 2 | 3
    return [i for i in range(1, 3 * 3 + 1)]


def create_board():
    # ""|""|""
    return [' ' for i in range(9)]


def print_board(brd):
    for i in range(3):
        print(' | '.join([str(brd[i]) for i in range(i * 3, i * 3 + 3)]))


def empty_squares():
    return ' ' in board


def player_name_mark():
    # {'X': 'Sway', 'O': 'Ivan'}
    players_gen = {}
    for i in range(2):
        name = input(f"Player {i + 1}, enter name: ")
        if i == 1:
            symbol = 'O' if players_gen.get('X') else 'X'
            players_gen[symbol] = name
        while i == 0:
            try:
                symbol = input(f"Player {i + 1}, enter mark (X) or (O): ")
                if symbol == 'X' or symbol == 'O':
                    players_gen[symbol] = name
                    break
                raise ValueError
            except ValueError:
                print('Mark can only be (X) or (O)')
    return players_gen


def valid_square(value):
    if value in range(1, 10) and board[value - 1] == ' ':
        return True
    return False


def choose_square(player):
    while True:
        try:
            square = input(f"{players[player]} -> Choose a valid square (1-9): ")
            value = int(square)
            if valid_square(value):
                break
            raise ValueError
        except ValueError:
            print('Not a number or not an empty square')
    return value - 1


def make_move(player):
    idx = choose_square(player)
    board[idx] = player

    if winner(idx, player):
        print(f'Winner is {players[player]}!!')
        print_board(board)
        raise SystemExit


def winner(square, player):
    # if square = 5, row_ind = 1, board[row] = [3, 4, 5]
    row_ind = square // 3
    row = board[row_ind * 3: (row_ind + 1) * 3]
    if all(symbol == player for symbol in row):
        return True
    # if square = 5, col_ind = 1, board[col] = [1, 5, 8]
    col_idx = square % 3
    col = [board[col_idx + i * 3] for i in range(3)]
    if all(symbol == player for symbol in col):
        return True
    # diagonals
    if square % 2 == 0:
        left_diag = [board[i] for i in [2, 4, 6]]
        if all(symbol == player for symbol in left_diag):
            return True
        right_diag = [board[i] for i in [0, 4, 8]]
        if all(symbol == player for symbol in right_diag):
            return True


def play():
    player = 'X'
    print_board(create_board_nums())
    while empty_squares():
        make_move(player)
        print_board(board)
        player = 'X' if player == 'O' else "O"

    if not empty_squares():
        print('DRAW')


if __name__ == "__main__":
    board = create_board()
    # players = player_name_mark()
    players = {'X': 'Sway', 'O': 'Ivan'}
    play()
