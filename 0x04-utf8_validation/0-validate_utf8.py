#!/usr/bin/python3
""" validUTF8: determines if a given data set represents a valid UTF-8 encoding """

def validUTF8(data):
    """
    Args:
        data - a list of integers with each integer representing 1 byte of data
    Return:
        True if data is valid UTF-8 encoding, else return False
    """

    data_length = len(data)
    for i in range(0, data_length):
        if data[i] <= 128:
            continue
        else:
            return False
    return True
