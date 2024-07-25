# UTF-8 Validation

This project contains a Python script to validate whether a given dataset represents a valid UTF-8 encoding.

## Usage

The main function `validUTF8(data)` checks if a given list of integers represents a valid UTF-8 encoding. The function returns `True` if the data is valid, and `False` otherwise.

### Example

```python
data = [197, 130, 1]
print(validUTF8(data))  # Expected output: True
