#!/usr/bin/python3
"""
    def canUnlockAll(boxes): Lockboxes function
    canUnlockAll(boxes) - true
"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
        method to determine if all the boxes
        can be opened.
        - A key with the same number as a box opens that box.
        - assume all keys are positive
        - there can be keys that do not have boxes
        - The first box boxes[0] is unlocked

        Args: boxes(list of list) -
            a list of boxes, where each box may
            contain keys to the other boxes.

        return: bool - True if all boxes
                can be opened, else return False
    """

    keys = []

    # Get the keys in the first box
    for key in boxes[0]:
        keys.append(key)

    # Use the keys in the first box to open the other boxes.
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys:
                keys.append(new_key)

    #keys_len = len(keys)
    boxes_len = len(boxes)
    #print(keys, keys_len, boxes_len)

    #if ((keys_len == (boxes_len - 1)) or (keys_len >= boxes_len)):
        #return True
    #return False

    for i in range(1, boxes_len):
        if i not in keys:
            return False
    return True
