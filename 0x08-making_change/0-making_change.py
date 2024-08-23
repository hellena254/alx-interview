#!/usr/bin/python3
"""
Module for making change problem
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to make up a given amount

    Args:
        coins (list): List of coin denominations
        total (int): The total amount to achieve with the coins

    Returns:
        int: Fewest number of coins needed to meet total, or -1 if not possible
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
