#!/usr/bin/env python3

import sys
import re

pattern = re.compile(r"(.)\1*")

for line in sys.stdin:
    s = line.rstrip("\n")
    print(pattern.sub(lambda m: f"{len(m.group(0))}{m.group(1)}", s))