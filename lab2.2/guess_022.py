#!/usr/bin/env python3

import sys

low = 1
high = 20
consistent = True

while True:
    line = sys.stdin.readline().strip()
    
    if not line:
        break
    
    if line == "higher":
        pass
    elif line == "lower":
        pass
    elif line == "correct":
        if low > high:
            consistent = False
        break
    else:
        guess = int(line)
        
        response = sys.stdin.readline().strip()
        
        if response == "higher":
            low = max(low, guess + 1)
        elif response == "lower":
            high = min(high, guess - 1)
        elif response == "correct":
            if guess < low or guess > high:
                consistent = False
            break
        
        if low > high:
            consistent = False
            break

if consistent:
    print("Bert can be trusted")
else:
    print("Bert is not to be trusted")