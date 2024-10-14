#!/usr/bin/python3

"""
Module to determine if all locked boxes can be unlocked.

The canUnlockAll function checks if all boxes in a list of locked boxes can be unlocked
based on the keys available inside the boxes.

Each box is numbered sequentially, and a key with the same number as a box opens that box.

Functions:
    - canUnlockAll(boxes): Determines if all boxes can be unlocked.

Usage Example:
    boxes = [[1], [2], [3], []]
    result = canUnlockAll(boxes)
    print(result)  # Output: True
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of lists): A list where each element is a list of keys in a box.
                               Each key is an integer representing a box it can unlock.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    n = len(boxes)
    unlocked = [False] * n  # Track which boxes are unlocked
    unlocked[0] = True  # The first box is always unlocked
    keys = [0]  # Start with the first box's keys

    while keys:
        box = keys.pop()  # Take a key (a box number)
        for key in boxes[box]:  # Explore all keys inside this box
            if key < n and not unlocked[key]:  # If the box is valid and not yet unlocked
                unlocked[key] = True  # Unlock the box
                keys.append(key)  # Add keys from the newly unlocked box

    # If all boxes are unlocked, return True, else False
    return all(unlocked)

# Example usage
if name == "main":
    boxes = [[1], [2], [3], []]
    print(canUnlockAll(boxes))  # Output: True
