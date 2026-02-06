#!/usr/bin/env python3

import sys

max_mark = 0
names = []
try:
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            try:
                if int(line.strip().split()[0]) > max_mark:
                    max_mark = int(line.strip().split()[0])
            except ValueError:
                print(f"Invalid mark {line.strip().split()[0]} encountered. Skipping.")
        
        for line in lines:
            try:
                if int(line.strip().split()[0]) == max_mark:
                    names.append(' '.join(line.strip().split()[1:]))
            except ValueError:
                continue
except FileNotFoundError:
    print(f"The file {sys.argv[1]} could not be opened.")
else:
    print(f"Best student(s): {', '.join(names)}")
    print(f"Best mark: {max_mark}")