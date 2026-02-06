#!/usr/bin/env python3

import sys

def to_upper_ascii(c):
    if 97 <= ord(c) <= 122:
        return chr(ord(c) - 32)
    return c


for line in sys.stdin:
    line = line.strip()

    if len(line) >= 2:
        line = to_upper_ascii(line[0]) + line[1:-1] + to_upper_ascii(line[-1])
        print(line)
