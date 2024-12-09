#!/usr/bin/python3

"""
Module to determine who wins the most rounds.
"""


def isWinner(x, nums):
    """Determine the winner of the prime number removal game."""
    if x < 1 or not nums:
        return None

    # Helper to precompute primes up to the maximum number in nums
    def sieve_of_eratosthenes(max_n):
        primes = [True] * (max_n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(max_n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, max_n + 1, i):
                    primes[j] = False
        return primes

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Convert the sieve to a list of primes for easier access
    prime_numbers = [i for i, is_prime in enumerate(primes) if is_prime]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
            continue

        # Count the number of primes up to n
        primes_count = sum(primes[:n + 1])
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
