#!/usr/bin/env python3

import sys
import string

def is_unique(s, list):
    for item in list:
        if item == s:
            return False
    list.append(s)
    return True

unique_list = []

for line in sys.stdin:
    s = line.strip().lower()
    for char in s:
        if char in string.punctuation:
            s = s.replace(char, '')
    tokens = s.split()
    for token in tokens:
        is_unique(token, unique_list)

print(len(unique_list))