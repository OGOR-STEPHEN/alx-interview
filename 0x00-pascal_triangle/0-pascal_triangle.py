#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n
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
    Print the Pascal's triangle in a formatted way
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if name == "main":
    print_triangle(pascal_triangle(5))
