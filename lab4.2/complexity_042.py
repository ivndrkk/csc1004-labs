import sys

for line in sys.stdin:
    s = line.strip()

    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    freqs = sorted(counts.values(), reverse=True)

    if len(freqs) <= 2:
        print(0)
    else:
        print(sum(freqs[2:]))
