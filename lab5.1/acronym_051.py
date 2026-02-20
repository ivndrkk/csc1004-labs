import sys

def acronym(name):
    if len(name) == 1 and "A" <= name <= "Z":
        return name

    result = ""
    i = 0
    while i < len(name) - 1:
        if i == 0 and "A" <= name[i] <= "Z":
            result += name[i]
        elif name[i] == " " and "A" <= name[i+1] <= "Z":
            result += name[i+1]
        i += 1
    return result

for line in sys.stdin:
    line = line.strip()
    print (acronym(line))