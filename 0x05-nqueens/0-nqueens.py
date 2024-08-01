#!/usr/bin/python3
"""Solving the famous N-Queen problem using backtracking (recursion inside loop)."""
import sys


class NQueen:
    """Class for solving the N-Queen problem."""

    def __init__(self, n):
        """Initialize the class with board size and solution list."""
        self.n = n
        self.x = [0 for _ in range(n + 1)]
        self.res = []

    def check_safety(self, k, i):
        """
        Check if it's safe to place a queen at position (k, i).
        
        Args:
            k: Current queen number (row index).
            i: Column index.
        
        Returns:
            bool: True if the queen can be placed, False otherwise.
        """
        for j in range(1, k):
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                return False
        return True

    def solve_nqueens(self, k):
        """
        Use backtracking to find all solutions for the N-Queen problem.
        
        Args:
            k: Current queen number (row index).
        
        Returns:
            list: List of all solutions.
        """
        for i in range(1, self.n + 1):
            if self.check_safety(k, i):
                self.x[k] = i
                if k == self.n:
                    solution = []
                    for j in range(1, self.n + 1):
                        solution.append([j - 1, self.x[j] - 1])
                    self.res.append(solution)
                else:
                    self.solve_nqueens(k + 1)
        return self.res


# Main
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueen(N)
res = queen.solve_nqueens(1)

for solution in res:
    print(solution)
