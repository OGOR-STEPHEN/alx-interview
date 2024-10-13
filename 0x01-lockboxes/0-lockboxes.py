#!/usr/bin/python

def canUnlockAll(boxes):
    """
    Determines if all boxes in a list of boxes can be unlocked.

    Each box may contain keys to unlock other boxes. The first box is unlocked by default,
    and we use the keys found in each box to unlock others. The goal is to check if
    all boxes can be unlocked.

    Parameters:
    boxes (list of lists): A list where each element represents a box containing a list of keys.

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

    # Total number of boxes
    n = len(boxes)

    # A list to track which boxes are unlocked. Initially, only box 0 is unlocked.
    unlocked = [False] * n
    unlocked[0] = True  # Box 0 is unlocked by default

    # Stack of keys we have collected, starting with box 0's keys
    keys = [0]

    # While there are still keys to process
    while keys:
        # Take one key to try to unlock the corresponding box
        current_key = keys.pop()

        # Try to unlock all boxes corresponding to the keys in the current box
        for key in boxes[current_key]:
            # Only unlock valid boxes and skip boxes that are already unlocked
            if key < n and not unlocked[key]:
                unlocked[key] = True  # Unlock the box
                keys.append(key)  # Add keys from this newly unlocked box to explore further

    # If all boxes are unlocked, return True; otherwise, return False
    return all(unlocked)
