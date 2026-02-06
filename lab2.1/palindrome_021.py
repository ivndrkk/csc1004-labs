#!/usr/bin/env python3

import sys

def is_palindrome(s):
    # Convert to lowercase and retain only alphanumeric characters
    s = ''.join(c for c in s.lower() if c.isalnum())
    return s == s[::-1]

for line in sys.stdin:
    s = line.strip()
    print(is_palindrome(s))