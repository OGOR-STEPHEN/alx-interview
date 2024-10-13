#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n  # Track which boxes are unlocked
    unlocked[0] = True  # The first box is unlocked by default
    keys = [0]  # Start with the keys from the first box

    while keys:
        current_key = keys.pop()  # Get the current key
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:  # Only unlock valid and locked boxes
                unlocked[key] = True  # Unlock the box
                keys.append(key)  # Add the keys from the newly unlocked box

    return all(unlocked)  # Check if all boxes are unlocked
