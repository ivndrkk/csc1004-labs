import sys

words = [
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine", "ten"
]

for line in sys.stdin:
    nums = line.split()
    text = [words[int(n)] for n in nums]
    print(" ".join(text))
