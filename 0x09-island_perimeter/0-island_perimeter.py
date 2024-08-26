#!/usr/bin/python3

"""
Island Perimeter Project
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island in a grid."""
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                # Check all four possible edges
                if row == 0 or grid[row - 1][col] == 0:  # Top edge
                    perimeter += 1
                if row == len(grid) - 1 or grid[row + 1][col] == 0:  # Bottom edge
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:  # Left edge
                    perimeter += 1
                if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:  # Right edge
                    perimeter += 1
    return perimeter
