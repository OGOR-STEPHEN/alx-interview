#!/usr/bin/python3

"""
Module for calculating the probability of change among items.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    if not coins:
        return -1

    # Sort coins for consistency in processing
    coins.sort()

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    result = dp[total]
    return result if result != float('inf') else -1
