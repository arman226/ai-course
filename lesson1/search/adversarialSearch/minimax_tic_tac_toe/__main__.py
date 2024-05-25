# minimax_tic_tac_toe.py

import math
import sys

sys.path.append("lesson1/search/adversarialSearch") 
from utils import play_game


def minimax(board, depth, is_max):
    """Minimax algorithm to find the best move"""
    score = evaluate(board)

    # If Maximizer has won the game return evaluated score
    if score == 10:
        return score

    # If Minimizer has won the game return evaluated score
    if score == -10:
        return score

    # If no more moves and no winner then it is a tie
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf

        # Traverse all cells
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    # Make the move
                    board[i][j] = "X"

                    # Call minimax recursively and choose the maximum value
                    best = max(best, minimax(board, depth + 1, not is_max))

                    # Undo the move
                    board[i][j] = "_"
        return best
    else:
        best = math.inf

        # Traverse all cells
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    # Make the move
                    board[i][j] = "O"

                    # Call minimax recursively and choose the minimum value
                    best = min(best, minimax(board, depth + 1, not is_max))

                    # Undo the move
                    board[i][j] = "_"
        return best


if __name__ == "__main__":
    play_game(minimax)
