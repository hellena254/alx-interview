# 0. Rotate 2D Matrix

## Description

This project involves implementing an in-place algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise. The matrix will be represented as a list of lists in Python, and the rotation must be performed without using any additional space, i.e., in-place.

## Files

- `0-rotate_2d_matrix.py`: Contains the function `rotate_2d_matrix(matrix)` that performs the matrix rotation.
- `main_0.py`: A test script to demonstrate the functionality of the `rotate_2d_matrix` function.

## Usage

To use the `rotate_2d_matrix` function, you can import it from the `0-rotate_2d_matrix.py` file and pass a 2D matrix as an argument. The matrix will be rotated in place, and no value is returned.

### Example

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

