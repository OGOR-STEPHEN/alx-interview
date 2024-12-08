#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): A list where each element is a list of keys
                                     contained in a box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list):
        return False  # Input must be a list of lists

    n = len(boxes)
    opened = [False] * n  # Track whether each box is opened
    opened[0] = True  # First box is always open
    keys = set(boxes[0])  # Start with the keys in the first box

    while keys:
        new_keys = set()  # Collect new keys during this iteration
        for key in keys:
            if 0 <= key < n and not opened[key]:  # Key is valid and box is not already opened
                opened[key] = True
                new_keys.update(boxes[key])  # Add new keys found in the box
        keys = new_keys  # Update keys with newly collected keys

    return all(opened)  # Check if all boxes are opened
