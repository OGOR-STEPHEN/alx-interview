#!/usr/bin/python3

"""
Module for calculating the probability of change among items.
"""


def makeChange(coins, total):
    def helper(remaining, index):
        if remaining == 0:
            return 0
        if remaining < 0 or index >= len(coins):
            return float('inf')
        use_coin = 1 + helper(remaining - coins[index], index)
        skip_coin = helper(remaining, index + 1)
        return min(use_coin, skip_coin)

    if total <= 0:
        return 0
    if not coins:
        return -1

    result = helper(total, 0)
    return result if result != float('inf') else -1
