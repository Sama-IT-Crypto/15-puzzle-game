import random
import os
BOARD_SIZE = 4
TARGET_ORDER = list(range(1, BOARD_SIZE * BOARD_SIZE)) + [0]

def generate_playable_board():
    flat_board = TARGET_ORDER[:]
    while True:
        random.shuffle(flat_board)
        if is_puzzle_solvable(flat_board):
            return [flat_board[i:i + BOARD_SIZE] for i in range(0, BOARD_SIZE ** 2, BOARD_SIZE)]

def is_puzzle_solvable(flat_board):
    inversions = 0
    for i in range(len(flat_board)):
        for j in range(i + 1, len(flat_board)):
            if flat_board[i] and flat_board[j] and flat_board[i] > flat_board[j]:
                inversions += 1
    zero_row_from_top = flat_board.index(0) // BOARD_SIZE
    if BOARD_SIZE % 2 == 1:
        return inversions % 2 == 0
    else:
        return (inversions + zero_row_from_top) % 2 == 1

def print_board(board):
    os.system("cls" if os.name == "nt" else "clear")
    print("\n15 Puzzle Game\n")
    for row in board:
        print(' '.join(f'{tile:2}' if tile != 0 else '  ' for tile in row))
    print("\nControls: W = up, S = down, A = left, D = right")

def find_empty_tile(board):
    for row_index in range(BOARD_SIZE):
        for col_index in range(BOARD_SIZE):
            if board[row_index][col_index] == 0:
                return col_index, row_index

def try_move_tile(board, direction):
    empty_x, empty_y = find_empty_tile(board)
    dx, dy = 0, 0
    if direction == 'w': dy = -1
    elif direction == 's': dy = 1
    elif direction == 'a': dx = -1
    elif direction == 'd': dx = 1
    else: return False
    new_x, new_y = empty_x + dx, empty_y + dy
    if 0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE:
        board[empty_y][empty_x], board[new_y][new_x] = board[new_y][new_x], board[empty_y][empty_x]
        return True
    return False

def is_board_in_winning_state(board):
    flat = [tile for row in board for tile in row]
    return flat == TARGET_ORDER

def play_puzzle_game():
    board = generate_playable_board()
    while True:
        print_board(board)
        if is_board_in_winning_state(board):
            print("Congratulations! You solved the puzzle! 🎉")
            break
        user_input = input("Your move (WASD): ").lower()
        try_move_tile(board, user_input)

play_puzzle_game()
