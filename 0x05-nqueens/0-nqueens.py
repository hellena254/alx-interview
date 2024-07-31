#!/usr/bin/python3

"""
Solving the famous N-Queen problem.
"""

import sys

def check_safety(board, row, col, N):
    """
    Check if its safe to place a queen at board[row][col]
    Args:
        board: 2d list rep the board
	row: row index
        col: col index
        N: size of the board
    Return: true if it's safe, false otherwise
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    # check upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check lower diagonal
    for i, j in zip(range(row, N, 1), range(col, N, 1)):
        if board[i][j] == 1:
            return False

    return True


def solution_nqueen(board, col, N, solutions):
    """
    Use backtracking to find all soln for the N queens problem
    Args:
        board: 2d list rep the chessboard
        col: current column index
        N: size of the bpard
	solutions: List to store all the possible solutions
    """
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(N):
        if check_safety(board, i, col, N):
            board[i][col] = 1
            solution_nqueen(board, col + 1, N, solutions)
            board[i][col] = 0


def solve_nqueens(N):
    """
    Solve the N queens problem and return all solutions
    Arg:
        N: size of the board
    Return:
        List of solutions, (queen position)
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solution_nqueen(board, 0, N, solutions)
    return solutions


def main():
    """
    Main function to handle command-line arguments and solve the process
    """
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
