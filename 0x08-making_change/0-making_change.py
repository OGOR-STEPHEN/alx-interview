#!/usr/bin/python3

"""
Module for calculating the probability of change among items.
"""

def makeChange(coins, total):
    if total <= 0:
        return 0
    if not coins:
        return -1

    # Initialize dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
