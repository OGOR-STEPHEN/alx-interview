#!/usr/bin/env python3
import sys

def is_valid(board, row, col):
    """
    Check if placing a queen at position (row, col) is safe.

    A position is considered safe if no other queens are placed in the same column,
    or on the same diagonal (both left and right) as the position.

    Parameters:
    - board (list): Current board state where index represents the row and value at index is the column.
    - row (int): Current row we are trying to place a queen.
    - col (int): Column in the current row to check for queen placement.

    Returns:
    - bool: True if the position is safe, False otherwise.
    """
    for i in range(row):
        # Check column and both diagonals
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    """
    Recursively solve the N Queens problem using backtracking.

    This function tries to place queens row by row and backtracks if a placement
    leads to an invalid state.

    Parameters:
    - N (int): Size of the chessboard (N x N).
    - row (int): Current row to place a queen.
    - board (list): List where index represents the row and value is the column of placed queens.
    - solutions (list): List to store all valid solutions.
    """
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col  # Place queen
            solve_nqueens(N, row + 1, board, solutions)  # Move to the next row
            board[row] = -1  # Backtrack by removing the queen


def nqueens(N):
    """
    Solves the N Queens problem and prints all unique solutions.

    Each solution is printed as a list of [row, col] positions for each queen.

    Parameters:
    - N (int): Size of the chessboard (N x N).
    """
    solutions = []
    board = [-1] * N  # Initialize board; -1 indicates no queen is placed in the row

    # Call the recursive function to solve the problem
    solve_nqueens(N, 0, board, solutions)

    # Print all solutions in the specified format
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Validate the input arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Attempt to convert the input argument to an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Ensure N is at least 4, as the problem is unsolvable for N < 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve and print solutions for the N Queens problem
    nqueens(N)
