#!/usr/bin/env python3

import sys
import re

for line in sys.stdin:
    s = line.rstrip("\n")
    print(max(re.findall(r"[A-Z]+", s), key=len))