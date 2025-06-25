#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    max_n = max(nums)

    # Sieve of Eratosthenes is used
    is_prime = [True] * (max_n + 1)
    is_prime[0:2] = [False, False]

    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(1, max_n + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
