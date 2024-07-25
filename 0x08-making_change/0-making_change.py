#!/usr/bin/python3

"""makeChange module"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins
    needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    n = len(coins)
    i = 0
    count = 0
    while i < n and total > 0:
        if coins[i] <= total:
            total -= coins[i]
            count += 1
        else:
            i += 1
    if total == 0:
        return count
    return -1
