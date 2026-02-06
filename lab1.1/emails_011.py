#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    first_name = ""
    last_name = ""
    temp = ""
    first_name, temp, mail, domain = line.split(".")
    i = 0
    while temp[i] not in "0123456789":
        last_name += temp[i]
        i += 1

    first_name = chr(ord(first_name[0]) - 32) + first_name[1:]
    last_name = chr(ord(last_name[0]) - 32) + last_name[1:]
    print(f"{first_name} {last_name}")