#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    :param boxes: list of lists where each list contains keys to other boxes.
    :return: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = boxes[0]

    for key in keys:
        if 0 <= key < n and not opened[key]:
            opened[key] = True
            keys.extend(boxes[key])

    return all(opened)
