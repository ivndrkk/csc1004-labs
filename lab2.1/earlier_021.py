#!/usr/bin/env python3

import sys

def earlier47(h, m):
    if m < 47:
        h -= 1
        m += 60
    m -= 47
    if h < 0:
        h += 24
    return str(f"{h:02d}:{m:02d}")

for line in sys.stdin:
    line = line.strip()
    h, m = map(int, line.split(":"))
    print(earlier47(h, m))