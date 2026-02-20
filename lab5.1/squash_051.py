import sys

def squash(s):
    if not s:
        return ""
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += f"{count}{s[i - 1]}"
            count = 1

    result += f"{count}{s[-1]}"
    return result

for line in sys.stdin:
    line = line.strip()
    print(squash(line))