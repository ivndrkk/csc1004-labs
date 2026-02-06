#!/usr/bin/env python3

import sys

nice = ["n", "i", "c", "e"]

def contains_nice(s):
    i = 0
    for char in s:
        if char in nice[:i]:
            return False
        elif char == nice[i]:
            i += 1
            if i == len(nice):
                return True
    return False

for line in sys.stdin:
    s = line.strip().lower()
    if contains_nice(s):
        print(line.strip())