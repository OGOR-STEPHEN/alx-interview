#!/usr/bin/python3


import sys


def print_solution(solution):
    """Print the solution in the required format"""
    print([[row, col] for row, col in enumerate(solution)])


def is_safe(solution, row, col):
    """Check if placing a queen at (row, col) is safe"""
    for r, c in enumerate(solution):
        if c == col or abs(c - col) == abs(r - row):
            return False


return True


def solve_nqueens(n, row, solution):
    """Recursive backtracking to find all solutions"""
    if row == n:
        print_solution(solution)
        return

    for col in range(n):

        if is_safe(solution, row, col):

            solve_nqueens(n, row + 1, solution + [col])


def main():
    """Main function to handle input and call solver"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)


if n < 4:
    print("N must be at least 4")

    sys.exit(1)
    solve_nqueens(n, 0, [])

if __name__ == "__main__":
    main()
