# Min Operations

This project contains a function to calculate the minimum number of operations required to get exactly `n` 'H' characters in a file, starting from a single 'H'. The allowed operations are "Copy All" and "Paste".

## Files

- `0-minoperations.py`: Contains the `minOperations` function.
- `0-main.py`: Main file for testing the `minOperations` function.
- `README.md`: This file.

## Function

### `minOperations(n)`

Calculates the fewest number of operations needed to result in exactly `n` 'H' characters in the file.

#### Arguments
- `n` (int): The target number of 'H' characters.

#### Returns
- `int`: The minimum number of operations, or 0 if `n` is impossible to achieve.

#### Example

```python
minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
# Output: Min number of operations to reach 4 characters: 4

n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
# Output: Min number of operations to reach 12 characters: 7
