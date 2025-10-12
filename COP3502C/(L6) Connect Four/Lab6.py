
def initialize_board(num_rows, num_cols):
    board = []
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            row.append('-')
        board.append(row)
    return board


def print_board(board):
    for row in reversed(board):
        print(' '.join(row))
    print()


def insert_chip(board, col, chip_type):
    for row in range(len(board)):
        if board[row][col] == '-':
            board[row][col] = chip_type
            return row


def check_if_winner(board, col, row, chip_type):
    num_rows = len(board)
    num_cols = len(board[0])

    # --- Check vertically ---
    count = 0
    for r in range(num_rows):
        if board[r][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # --- Check horizontally ---
    count = 0
    for c in range(num_cols):
        if board[row][c] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    return False


if __name__ == "__main__":
    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))

    board = initialize_board(height, length)
    print_board(board)

    print("Player 1: x")
    print("Player 2: o\n")

    turn = 0
    total_moves = 0
    max_moves = height * length
    winner_found = False

    while total_moves < max_moves:
        if turn % 2 == 0:
            player = 1
            chip = 'x'
        else:
            player = 2
            chip = 'o'

        col = int(input(f"Player {player}: Which column would you like to choose? "))
        row = insert_chip(board, col, chip)
        print_board(board)

        if check_if_winner(board, col, row, chip):
            print(f"Player {player} won the game!")
            winner_found = True
            break

        turn += 1
        total_moves += 1

    if not winner_found:
        print("Draw. Nobody wins.")




