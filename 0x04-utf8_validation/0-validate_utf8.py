#!/usr/bin/python3

"""
Script to validate if a given dataset represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the first bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Extract the 8 least significant bits
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                continue  # 1-byte character
            elif (byte & 0xE0) == 0xC0:
                num_bytes = 1  # 2-byte character
            elif (byte & 0xF0) == 0xE0:
                num_bytes = 2  # 3-byte character
            elif (byte & 0xF8) == 0xF0:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid first byte
        else:
            # Check that the byte starts with 10xxxxxx
            if (byte & 0xC0) != 0x80:
                return False
            num_bytes -= 1

    # Ensure all characters have been completed
    return num_bytes == 0
