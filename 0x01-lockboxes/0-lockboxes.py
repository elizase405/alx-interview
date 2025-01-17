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

    boxes_len = len(boxes)

    # Use the keys in the first box to open the other boxes.
    for key in keys:
        # handle keys that are out of list range
        if key >= boxes_len:
            continue
        else:
            for new_key in boxes[key]:
                if new_key not in keys:
                    keys.append(new_key)

    # if all the keys from box 1 to
    # boxes_len - 1 are in the keys list
    # then it is an unlocked box.
    for i in range(1, boxes_len):
        if i not in keys:
            return False
    return True
