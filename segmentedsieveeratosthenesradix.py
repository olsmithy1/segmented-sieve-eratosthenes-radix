# -*- coding: utf-8 -*-
"""
Created on Tue March 19 11:05:43 2023

@author: Sean Smith
"""

def sieve_eratosthenes(n):
    # Initialize a list of booleans to mark numbers as prime or not
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Using Sieve of Eratosthenes to mark numbers as prime or not
    for num in range(2, int(n**0.5) + 1):
        if is_prime[num]:
            for j in range(num*num, n + 1, num):
                is_prime[j] = False

    # Return a list of prime numbers (excluding 0 and 1)
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

def segmented_sieve_radix(L, R):
    # Generate primes up to sqrt(R)
    sqrt_R = int(R ** 0.5)
    primes = sieve_eratosthenes(sqrt_R)

    # Initialize is_prime_segment array for the current segment
    is_prime_segment = [True] * (R - L + 1)

    # Mark multiples of primes in the current segment using radix sort
    for prime in primes:
        start = max(prime * prime, L)  # First multiple in the segment
        for num in range(start, R + 1, prime):
            if num >= 2 and num - L >= 0:  # Ensure the index is valid
                is_prime_segment[num - L] = False

    # Collect prime numbers in the current segment, excluding 0 and 1
    segment_primes = [i + L for i in range(R - L + 1) if is_prime_segment[i] and i + L > 1]

    return segment_primes

if __name__ == "__main__":
    L, R = 0, 200
    segment_primes = segmented_sieve_radix(L, R)
    print("Prime numbers in the segment [{}, {}]:".format(L, R), segment_primes)
