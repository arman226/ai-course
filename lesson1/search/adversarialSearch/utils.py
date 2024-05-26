import math


def print_board(board):
    """Prints the Tic-Tac-Toe board"""

    print("BOARD")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_moves_left(board):
    """Checks if there are moves left on the board"""
    for row in board:
        if "_" in row:
            return True
    return False

def evaluate(board):
    """Evaluates the board to check for a win or tie"""
    # Check rows for a win
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'X':
                return 10
            elif board[row][0] == 'O':
                return -10

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    # No winner
    return 0

def find_best_move(board, minimax):
    """Finds the best move for the computer"""
    best_val = -math.inf
    best_move = (-1, -1)

    # Traverse all cells
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                # Make the move
                board[i][j] = "X"

                # Compute evaluation function for this move
                move_val = minimax(board, 0, False)

                # Undo the move
                board[i][j] = "_"

                # If the value of the current move is more than the best value, update best
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move #this returns a tuple (coordinates)

def play_game(minimax):
    """Main function to play the game"""
    board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]
    print_board(board)

    for _ in range(9):
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] != "_":
            print("Invalid move. Try again.")
            continue
        board[row][col] = "O"
        print_board(board)

        if evaluate(board) == -10:
            print("O wins!")
            return

        if not is_moves_left(board):
            print("It's a tie!")
            return

        best_move = find_best_move(board, minimax)
        board[best_move[0]][best_move[1]] = "X"
        print_board(board)

        if evaluate(board) == 10:
            print("X wins!")
            return

        if not is_moves_left(board):
            print("It's a tie!")
            return
