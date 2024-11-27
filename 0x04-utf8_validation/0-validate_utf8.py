#!/usr/bin/python3

"""
Script to validate if a given dataset represents a valid UTF-8 encoding.
"""

from typing import List

def validUTF8(data: List[int]) -> bool:
    """
    Determines if a given list of integers represents a valid UTF-8 encoding.
    """
    num_bytes = 0  # Counter for continuation bytes needed

    for byte in data:
        byte &= 0xFF  # Ensure only the last 8 bits are considered

        if num_bytes == 0:
            # Determine the type of UTF-8 character by inspecting leading bits
            if byte >> 5 == 0b110:  # 2-byte character
                num_bytes = 1
            elif byte >> 4 == 0b1110:  # 3-byte character
                num_bytes = 2
            elif byte >> 3 == 0b11110:  # 4-byte character
                num_bytes = 3
            elif byte >> 7 != 0:  # 1-byte character should start with 0xxxxxxx
                return False
        else:
            # Check that each continuation byte starts with 10xxxxxx
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    # If all continuation bytes are matched, it should return true
    return num_bytes == 0

# Test with the example provided
test_data = [65]
print(validUTF8(test_data))

# Test with the example provided
test_data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(test_data))

# Test with the example provided
test_data = [229, 65, 127, 256]
print(validUTF8(test_data))  # Expected output: True
