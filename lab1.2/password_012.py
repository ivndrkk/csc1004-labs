#!/usr/bin/env python3
import sys

for password in sys.stdin:
    password = password.rstrip("\n")
    classes_count = [False, False, False, False]
    for ch in password:
        if ch.islower():
            classes_count[0] = True
        elif ch.isupper():
            classes_count[1] = True
        elif ch.isdigit():
            classes_count[2] = True
        else:
            classes_count[3] = True
    print(sum(classes_count))