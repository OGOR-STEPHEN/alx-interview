#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): Denominations of coins available.
        total (int): Target amount.

    Returns:
        int: Fewest number of coins to make up the total, or -1 if not possible.
    """
    if total <= 0:
        return 0
    
    # Initialize dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case
    
    # Update dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # Return result
    return dp[total] if dp[total] != float('inf') else -1
