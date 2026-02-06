#!/usr/bin/env python3
import sys

def contains(left, right):
    for lchar in left:
        if lchar in right:
            right = right.replace(lchar, "", 1)
        else:
            return False
    return True

for line in sys.stdin:
    line = line.strip()
    line = "".join(chr(ord(c)+32) if 'A' <= c <= 'Z' else c for c in line)
    left, right = line.split()
    print(contains(left, right))
