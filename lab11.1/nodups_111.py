import sys
import string

seen = []
lines = []

for line in sys.stdin.readlines():
    lines.append(f"{line.strip()}\n")

for line in lines:
    new_line = ""
    for word in line.split():
        original = word 
        end = ""
        while len(word) > 0 and word[-1] in string.punctuation:
            end = word[-1] + end
            word = word[:-1]

        clean = word.lower()

        if clean not in seen:
            seen.append(clean)
            new_line = new_line + " " + original
        else:
            new_line = new_line + " ." + end

    print(new_line.strip())