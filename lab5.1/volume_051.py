import sys

def volumeChanger(MIN, MAX, CURRENT, COMMAND):
    if COMMAND == 'UP':
        if CURRENT < MAX:
            CURRENT += 1
    elif COMMAND == 'DOWN':
        if CURRENT > MIN:
            CURRENT += 1
    return CURRENT

result = None
config = sys.stdin.readline()
min, max, current = config.strip().split()

for line in sys.stdin:
    line = line.strip()
    result = volumeChanger(min, max, current, line)
    
print(result)