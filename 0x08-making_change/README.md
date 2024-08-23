# 0x08-making_change

## Project: 0. Change comes from within

This project involves solving the classic "coin change problem" using dynamic programming in Python. The objective is to determine the fewest number of coins needed to make up a given total amount from a list of coin denominations.

### Problem Description

Given a pile of coins of different values, determine the minimum number of coins needed to meet a given total amount. 

- **Function Prototype**: `def makeChange(coins, total):`
- **Parameters**:
  - `coins` (list): A list of integers representing the values of the coins available.
  - `total` (int): The total amount to achieve with the coins.
- **Returns**:
  - The fewest number of coins needed to meet the total.
  - If the total is 0 or less, return `0`.
  - If the total cannot be met by any number of coins you have, return `-1`.

### Example

```python
makeChange([1, 2, 25], 37)
# Output: 7 (25 + 10 + 2)

makeChange([1256, 54, 48, 16, 102], 1453)
# Output: -1 (No combination can make up the total)
