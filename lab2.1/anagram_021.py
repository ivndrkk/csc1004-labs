#!/usr/bin/env python3

import sys

def are_anagrams(str1, str2):
    for char in str1:
        if char not in str2:
            return False
        else:
            str2 = str2.replace(char, '', 1)
    return len(str2) == 0

for line in sys.stdin:
    str1,str2 = line.strip().split()
    print(are_anagrams(str1, str2))