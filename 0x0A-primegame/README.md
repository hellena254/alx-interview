# Prime Game

## Description

The Prime Game is a competitive game involving two players, Maria and Ben. Given a set of consecutive integers starting from 1 up to and including `n`, players take turns choosing a prime number from the set and removing that number and all its multiples. The player who cannot make a move loses the game. Maria always goes first, and both players play optimally.

This project implements a solution to determine the winner after multiple rounds of the game.

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/hellena254/alx-interview.git
cd alx-interview/0x0A-primegame
```

Ensure that the Python files are executable:

```bash
chmod +x 0-prime_game.py
```

## Usage

To use the `isWinner` function, import it into your Python script and call it with the required parameters:

```python
from 0-prime_game import isWinner

x = 3
nums = [4, 5, 1]
winner = isWinner(x, nums)
print(f"The winner is: {winner}")
```

### Example

```bash
$ ./main_0.py
Winner: Ben
```

### Explanation

For the example provided:

- **First round** (`n = 4`):
  - Maria picks `2` and removes `2, 4`, leaving `1, 3`.
  - Ben picks `3` and removes `3`, leaving `1`.
  - Ben wins because there are no prime numbers left for Maria to choose.
  
- **Second round** (`n = 5`):
  - Maria picks `2` and removes `2, 4`, leaving `1, 3, 5`.
  - Ben picks `3` and removes `3`, leaving `1, 5`.
  - Maria picks `5` and removes `5`, leaving `1`.
  - Maria wins because there are no prime numbers left for Ben to choose.
  
- **Third round** (`n = 1`):
  - Ben wins because there are no prime numbers for Maria to choose.

Result: Ben wins 2 out of 3 rounds.

## Functions

### `sieve_of_eratosthenes(max_n)`

Generates a list of all prime numbers up to `max_n` using the Sieve of Eratosthenes algorithm.

- **Parameters**:
  - `max_n` (int): The upper limit for generating prime numbers.
  
- **Returns**:
  - List of prime numbers up to `max_n`.

### `isWinner(x, nums)`

Determines the winner after `x` rounds of the Prime Game.

- **Parameters**:
  - `x` (int): The number of rounds.
  - `nums` (list): A list containing the `n` value for each round.
  
- **Returns**:
  - The name of the player with the most wins ("Maria" or "Ben").
  - If there is a tie or no clear winner, returns `None`.

## Files

- `0-prime_game.py`: Contains the implementation of the `sieve_of_eratosthenes` and `isWinner` functions.
- `main_0.py`: Example script to test the `isWinner` function.

*Happy Learning :)*

