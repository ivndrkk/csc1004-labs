#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()[1:len(line)-2]
    if line:
        print(line)