#!/usr/bin/env python3
import sys

max_length = 0
lines = []
for line in sys.stdin:
    line = line.rstrip("\n")
    if len(line) > max_length:
        max_length = len(line)
    lines.append(line)

for line in lines:
    print(f"{line:^{max_length}}")