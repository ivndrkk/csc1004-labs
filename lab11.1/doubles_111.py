import sys

lines = []
countVow = {}
vowels = ['a', 'e', 'i', 'o', 'u']
max_double_vowels = ""

def isDoubleVowel(s:str):
    if s[0] == s[1]:
        return True
    else:
        return False

for line in sys.stdin.readlines():
    line = line.strip().lower()
    lines.append(line)


for line in lines:
    countVow[line] = 0
    x = 0
    while x < len(line)-1:
        if line[x] in vowels:
            if isDoubleVowel(line[x:x+2]):
                countVow[line] += 1
                x += 2
            else:
                x += 1
        else:
            x += 1


for s in countVow:
    if max_double_vowels == "":
        max_double_vowels = s
    if countVow[s] > countVow[max_double_vowels]:
        max_double_vowels = s

print(max_double_vowels)




