import sys

expected = sys.stdin.readline().rstrip("\n")
actual = sys.stdin.readline().rstrip("\n")

i = j = 0
sticky = set()

while i < len(expected) and j < len(actual):
    if expected[i] == actual[j]:
        if j + 1 < len(actual) and actual[j] == actual[j + 1]:
            sticky.add(expected[i])
            j += 2
        else:
            j += 1
        i += 1
    else:
        sticky.add(actual[j])
        j += 1

print("".join(sorted(sticky)))