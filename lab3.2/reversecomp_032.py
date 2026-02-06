#!/usr/bin/env python3
import sys

def binsearch(query, sorted_list):
    '''Return True if query in sorted_list otherwise False.'''

    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid] < query:
            low = mid + 1
        elif sorted_list[mid] > query:
            high = mid - 1
        else:
            return True
    return False

words = [line.strip() for line in sys.stdin]

words_lower_sorted = sorted([word.lower() for word in words])

result = [word for word in words if len(word) >= 5 and binsearch(word.lower()[::-1], words_lower_sorted)]

print(result)
