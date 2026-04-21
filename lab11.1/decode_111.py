import sys

vowels = ["a","e","i","o","u"]

def decode(s):
    decoded = ""
    i = 0
    while i < len(s):
        if s[i] in vowels and s[i+1] == "p" and s[i+2] == s[i]:
            decoded += s[i]
            i += 3
        else:
            decoded += s[i]
            i += 1
    return decoded

for line in sys.stdin.readlines():
    print(decode(line.strip()))