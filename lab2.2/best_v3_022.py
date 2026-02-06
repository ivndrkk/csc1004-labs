#!/usr/bin/env python3

import sys

max_mark = 0
name = ""
try:
    with open(sys.argv[1], 'r') as file:
        for line in file:
            try:
                if int(line.strip().split()[0]) > max_mark:
                        max_mark = int(line.strip().split()[0])
                        name = line.strip().split()[1:]
            except ValueError:
                print(f"Invalid mark {line.strip().split()[0]} encountered. Skipping.")
except FileNotFoundError:
    print(f"The file {sys.argv[1]} could not be opened.")
else:
    print(f"Best student: {' '.join(name)}")
    print(f"Best mark: {max_mark}")