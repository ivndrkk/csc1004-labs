import sys

mapping = {}

with open(sys.argv[1]) as f:
    for line in f:
        eng, trans = line.split()
        mapping[eng] = trans

words = [
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine", "ten"
]

# process stdin
for line in sys.stdin:
    out = []
    for n in line.split():
        eng_word = words[int(n)]
        out.append(mapping[eng_word])
    print(" ".join(out))
