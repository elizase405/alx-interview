#!/usr/bin/python3
""" validUTF8: determines if a given data set
               represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Args:
        data - a list of integers with each integer representing 1 byte of data
    Return:
        True if data is valid UTF-8 encoding, else return False
    """

    for byte in data:
        data_bit = format(byte, '08b')
        if data_bit.startswith('0') \
        or data_bit.startswith('10') and len(data_bit) == 8\
        or data_bit.startswith('110') \
        or data_bit.startswith('1110') \
        or data_bit.startswith('11110'):
            continue
        else:
            return False
    return True
