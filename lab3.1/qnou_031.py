#!/usr/bin/env python3
import sys

words = [line.strip() for line in sys.stdin if line.strip()]

q_no_u = [
    w for w in words
    if any(
        c == 'q' and (i == len(w) - 1 or w[i + 1].lower() != 'u')
        for i, c in enumerate(w.lower())
    )
]

print(f"Words with q but no u: {q_no_u}")
