#!/usr/bin/env python3

import sys

def numcomps(list):
    print(f"Non-multiples of 3 replaced: {[n if not n % 3 else 0 for n in list]}")

for num in sys.stdin.readlines():
    num = int(num.strip())

    numlist = []
    for i in range(1, num + 1):
        numlist.append(i)

    numcomps(numlist)