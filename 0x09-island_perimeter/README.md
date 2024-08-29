# 0x09. Island Perimeter

## Description

This project involves calculating the perimeter of an island represented in a grid. The grid is a 2D array where each cell can either be water (`0`) or land (`1`). The objective is to create a function, `island_perimeter`, that returns the perimeter of the island described in the grid.

### Concepts and Skills Required

- **2D Arrays (Matrices):** Understanding how to access and iterate over elements in a 2D array. Knowing how to navigate through adjacent cells (horizontally and vertically) is crucial.
- **Conditional Logic:** Applying conditions to determine whether a cell contributes to the perimeter of the island.
- **Counting Techniques:** Developing a method to count the edges that contribute to the island's perimeter.
- **Python Programming:** Utilizing nested loops for iterating over grid cells and conditional statements to check the status of adjacent cells.

## Task

### 0. Island Perimeter

#### Objective

Write a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`.

#### Input

- `grid` is a list of lists of integers:
  - `0` represents water
  - `1` represents land
- Each cell is a square with a side length of 1.
- Cells are connected horizontally or vertically (not diagonally).
- The grid is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or none).
- The island does not have "lakes" (water inside that isn't connected to the water surrounding the island).

#### Output

- The function should return an integer representing the perimeter of the island.

#### Example

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```

## Implementation

To solve the problem, you need to:

1. **Iterate** through each cell in the grid.
2. **Identify** land cells (`1`) and calculate the number of edges that contribute to the perimeter:
   - Check each adjacent cell (top, bottom, left, right).
   - If the adjacent cell is water (`0`) or is out of bounds, the edge contributes to the perimeter.
3. **Sum** all contributing edges to get the total perimeter.

## Usage

To test your function, you can run the provided `0-main.py` file:

```bash
chmod +x 0-main.py
./0-main.py
```

## Resources

- **Python Official Documentation:** For understanding nested lists and iterating through 2D arrays.
- **GeeksforGeeks Articles:** Guides on working with multi-dimensional arrays in Python.
- **YouTube Tutorials:** Videos explaining 2D arrays and lists in Python.
