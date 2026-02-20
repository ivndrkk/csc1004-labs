import sys

def volumeChanger(MIN, MAX, CURRENT, COMMAND):
    if COMMAND == 'UP' and CURRENT < MAX:
        CURRENT += 1
    elif COMMAND == 'DOWN' and CURRENT > MIN:
        CURRENT -= 1
    return CURRENT

config = sys.stdin.readline().strip()
MIN, CURRENT, MAX = map(int, config.split())

current_volume = CURRENT

for line in sys.stdin:
    command = line.strip()
    current_volume = volumeChanger(MIN, MAX, current_volume, command)

print(current_volume)