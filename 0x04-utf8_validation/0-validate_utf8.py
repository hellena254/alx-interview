#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    Arg: data- a list of integers
    Return: boolean
        True if data is a valid UTF-8 encoding, else return False
    """
    n_bytes = 0
    m1 = 1 << 7
    m2 = 1 << 6

    for i in data:
        # handle the 8 least significant bits of each integer
        bin_rep = format(i, '08b')

        if n_bytes == 0:
            for bit in bin_rep:
                if(int(bit) & m1) == 0:
                    break

                n_bytes += 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False

        else:
            if not (int(bin_rep[0]) == 1 and int(bin_rep[1]) == 0):
                return False

        n_bytes -= 1

    return n_bytes == 0
