#!/usr/bin/python3
"""
Prime Game
"""


def sieve(n):
    """ Return a list of primes less than or
        equal to n using the Sieve of Eratosthenes. """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_list = [p for p in range(2, n + 1) if is_prime[p]]
    return prime_list


def prime_count(n):
    """ Returns the number of primes up to n using a sieve. """
    primes = sieve(n)
    return len(primes)


def isWinner(x, nums):
    """ Determines the winner of the game after x rounds. """
    if x < 1 or not nums:
        return None

    # Number of rounds Maria and Ben win
    maria_wins = 0
    ben_wins = 0

    # Process each game
    for n in nums:
        primes = prime_count(n)
        # Maria wins if the number of primes is odd, Ben wins if even
        if primes % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
