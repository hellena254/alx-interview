#!/usr/bin/python3
"""
Prime Gamer
"""


def sieve_of_eratosthenes(max_n):
    """
    Generate a list of prime numbers up to max_n
    """
    primes = [True] * (max_n + 1)
    p = 2
    while p * p <= max_n:
        if primes[p]:
            for i in range(p * p, max_n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, max_n + 1) if primes[p]]


def isWinner(x, nums):
    """
    Determine the winner after x rounds of the game
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        prime_count = sum(1 for p in primes if p <= n)
        if prime_count % 2 == 1:
            wins["Maria"] += 1
        else:
            wins["Ben"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None
