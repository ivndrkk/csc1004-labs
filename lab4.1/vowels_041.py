import sys

vowels = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}

for line in sys.stdin:
    line = line.strip().lower()
    for char in line:
        if char in vowels:
            vowels[char] += 1

width = len(str(max(vowels.values())))

for vowel, count in sorted(vowels.items(), key=lambda x: x[1], reverse=True):
    print(f"{vowel}: {count:{width}}")
