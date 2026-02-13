import sys
import string

words = {}

for line in sys.stdin:
    tokens = line.strip().split()
    for word in tokens:
        word = word.strip(string.punctuation)
        if word.lower() in words:
            words[word.lower()] += 1
        else:
            words[word.lower()] = 1


for word in sorted(words):
    print(f"{word}: {words[word]}")
