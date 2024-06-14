#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All: You can copy all the characters
    present in the file (if the file is empty, then nothing is copied).
    Paste: You can paste the copied characters at the end of the file.
    Given a number n, you have to get exactly n H characters
    on the file by performing the minimum number of operations.
    Write a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
    Returns an integer
    """
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return n
