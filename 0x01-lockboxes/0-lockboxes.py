#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Parameters:
    boxes (list of lists): A list where each element is a list of keys contained in that box.
                           The box at index 0 is always unlocked.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.

    Example:
    >>> canUnlockAll([[1], [2], [3], [4], []])
    True

    >>> canUnlockAll([[1, 3], [3, 0, 1], [2], [0]])
    True

    >>> canUnlockAll([[1, 2], [0], [0, 1]])
    False
    """
    n = len(boxes)
    unlocked = [False] * n  # Track unlocked boxes
    unlocked[0] = True  # Box 0 is always unlocked
    keys = [0]  # Start with the keys from box 0

    while keys:
        current_key = keys.pop()  # Get the next key to process
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:  # Check if key is valid and unlock new boxes
                unlocked[key] = True  # Unlock the box
                keys.append(key)  # Add keys from the newly unlocked box

    return all(unlocked)  # Check if all boxes are unlocked
