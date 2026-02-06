#!/usr/bin/env python3

import sys

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

for num in sys.stdin.readlines():
    n = int(num.strip())
    numbers = [i for i in range(2, n + 1)]
    print(f"Primes: {[number for number in numbers if is_prime(number)]}")