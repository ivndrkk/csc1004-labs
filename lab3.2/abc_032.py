#!/usr/bin/env python3
import sys

numbers = list(map(int, input().split()))
order = input().strip()

sorted_numbers = sorted(numbers)

letter_to_value = {
    'A': sorted_numbers[0],
    'B': sorted_numbers[1],
    'C': sorted_numbers[2],
    'D': sorted_numbers[3],
    'E': sorted_numbers[4],
    'F': sorted_numbers[5]
}

result = [str(letter_to_value[letter]) for letter in order]
print(' '.join(result))
