#!/usr/bin/env python3
import sys

max_length = 0
rows = []

for line in sys.stdin:
    tokens = line.split()
    club = " ".join(tokens[1:-8])
    max_length = max(max_length, len(club))
    rows.append((tokens[0], club, tokens[-8:]))

print(f"{'POS':>3} {'CLUB':<{max_length}}  P  W  D  L GF GA  GD PTS")

for pos, club, stats in rows:
    print(
        f"{pos:>3} {club:<{max_length}} "
        f"{stats[0]:>2} {stats[1]:>2} {stats[2]:>2} {stats[3]:>2} "
        f"{stats[4]:>2} {stats[5]:>2} {stats[6]:>3} {stats[7]:>3}"
    )
