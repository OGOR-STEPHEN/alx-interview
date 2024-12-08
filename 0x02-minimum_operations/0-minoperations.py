#!/usr/bin/python3

"""
Module to determine the minimum number of operations for'H' characters.

Functions:
    - minOperations(n): Determines the minimum number of operations needed.

Usage Example:
    result = minOperations(9)
    print(result)  # Output: 6
"""


def minOperations(n):
    """

    Args:
    n (int): The target number of 'H' characters to achieve.
    Returns:
    int: The minimum number of operations required, or 0 if it's impossible.
    """
    if n <= 1:
        return 0

    operations = 0  # Initialize the count of operations
    divisor = 2

    # Continue until we reduce n to 1 by factoring out divisors
    while n > 1:
        while n % divisor == 0:  # While n is divisible by the current divisor
            operations += divisor
            n //= divisor  # Reduce n by dividing it by the divisor
        divisor += 1  # Move to the next potential divisor

    return operations

# Example usage


if __name__ == "__main__":
    n = 9
    print(minOperations(n))  # Output: 6
