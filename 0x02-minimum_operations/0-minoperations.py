#!/usr/bin/python3

"""
Module to determine the minimum number of operations required to achieve a desired number of 'H' characters.

The `minOperations` function computes the fewest number of Copy All and Paste operations required to get
exactly `n` 'H' characters, starting with a single 'H'.

Functions:
    - minOperations(n): Determines the minimum number of operations needed.

Usage Example:
    result = minOperations(9)
    print(result)  # Output: 6
"""

def minOperations(n):
    """
    Determines the fewest number of operations required to achieve exactly n 'H' characters
    using only "Copy All" and "Paste" operations.

    Args:
        n (int): The target number of 'H' characters to achieve.

    Returns:
        int: The minimum number of operations required, or 0 if it's impossible.
    """
    if n <= 1:
        return 0  # If n is 1 or less, no operations are needed or possible to achieve more than one 'H'

    operations = 0  # Initialize the count of operations
    divisor = 2  # Start checking for divisors from 2 (the smallest prime number)

    # Continue until we reduce n to 1 by factoring out divisors
    while n > 1:
        while n % divisor == 0:  # While n is divisible by the current divisor
            operations += divisor  # Add the divisor to the operation count (one copy all and paste)
            n //= divisor  # Reduce n by dividing it by the divisor
        divisor += 1  # Move to the next potential divisor

    return operations

# Example usage
if __name__ == "__main__":
    n = 9
    print(minOperations(n))  # Output: 6
