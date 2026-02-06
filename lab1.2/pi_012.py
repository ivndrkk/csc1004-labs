#!/usr/bin/env python3

import sys
import math

for line in sys.stdin:
    n = int(line.strip())
    print(f"{math.pi:.{n}f}")