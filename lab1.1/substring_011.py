#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    for char in line:
        if 65 <= ord(char) <= 90:
            line = line.replace(char, chr(ord(char) + 32), 1)
    
    left, right = line.split(" ")
    print(left in right)