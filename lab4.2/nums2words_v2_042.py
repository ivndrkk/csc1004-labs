import sys

words = [
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine", "ten"
]

for line in sys.stdin:
    out = []
    for n in line.split():
        n = int(n)
        if 0 <= n <= 10:
            out.append(words[n])
        else:
            out.append("unknown")
    print(" ".join(out))
