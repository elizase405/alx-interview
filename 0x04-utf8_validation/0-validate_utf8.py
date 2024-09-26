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

    1-byte Sequence: 0xxxxxxx
    2-byte Sequence: 110xxxxx 10xxxxxx
    3-byte Sequence: 1110xxxx 10xxxxxx 10xxxxxx
    4-byte Sequence: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

    0x80 is 10000000
    0xC0 is 11000000
    0xE0 is 11100000
    0xF0 is 11110000
    """

    i = 0
    while i < len(data):
        if data[i] & 0x80 == 0x00:
            i += 1
        elif data[i] & 0xE0 == 0xC0:
            if i + 1 >= len(data) or data[i + 1] & 0xC0 != 0x80:
                return False
            i += 2
        elif data[i] & 0xF0 == 0xE0:
            if i + 2 >= len(data) or data[i + 1] & 0xC0 != 0x80 \
                                  or data[i + 2] & 0xC0 != 0x80:
                return False
            i += 3
        elif data[i] & 0xF8 == 0xF0:
            if i + 3 >= len(data) or data[i + 1] & 0xC0 != 0x80 \
                                  or data[i + 2] & 0xC0 != 0x80 \
                                  or data[i + 3] & 0xC0 != 0x80:
                return False
            i += 4
        else:
            return False
    return True
