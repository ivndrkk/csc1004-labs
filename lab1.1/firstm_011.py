#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    print(line.replace("m", "M", 1))