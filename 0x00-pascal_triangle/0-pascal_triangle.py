#!/usr/bin/python3


"""
This module defines a function pascal_triangle which generates
Pascal's Triangle up to a given number of rows, and a helper function
print_triangle to print the triangle in a formatted way.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        List[List[int]]: A list of lists where each inner list represents
        a row of Pascal's Triangle.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize the first row of the triangle
    
    for i in range(1, n):
        row = [1]  # Each row starts with a 1
        for j in range(1, i):
            # Add the sum of the two numbers above this position
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Each row ends with a 1
        triangle.append(row)
    
    return triangle


def print_triangle(triangle):
    """
    Print the Pascal's Triangle in a formatted way.

    Args:
        triangle (List[List[int]]): A list of lists where each inner list
        represents a row of Pascal's Triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
