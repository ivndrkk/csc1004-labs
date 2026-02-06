#!/usr/bin/env python3

import sys

def numcomps(list):
    print(f"Multiples of 3: {[n for n in list if not n % 3]}")
    print(f"Multiples of 3 squared: {[n**2 for n in list if not n % 3]}")
    print(f"Multiples of 4 doubled: {[n * 2 for n in list if not n % 4]}")
    print(f"Multiples of 3 or 4: {[n for n in list if not n % 3 or not n % 4]}")
    print(f"Multiples of 3 and 4: {[n for n in list if not n % 3 and not n % 4]}")

for num in sys.stdin.readlines():
    num = int(num.strip())

    numlist = []
    for i in range(1, num + 1):
        numlist.append(i)

    numcomps(numlist)