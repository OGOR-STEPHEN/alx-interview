#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a 2D grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.
    
    Args:
        grid (list of list of int): A rectangular 2D grid where:
            - 0 represents water.
            - 1 represents land.
            - Cells are connected horizontally/vertically.
            - Grid is surrounded by water.
    
    Returns:
        int: The perimeter of the island.
    
    Note:
        The grid contains only one island (or none).
        The island does not have any lakes.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Check top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check bottom
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
