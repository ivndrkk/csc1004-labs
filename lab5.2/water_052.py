import sys

line = list(map(int, sys.stdin.readline().split()))

left = 0
right = len(line) - 1
max_water = 0

while left < right:
    height = min(line[left], line[right])
    width = right - left
    max_water = max(max_water, height * width)

    if line[left] < line[right]:
        left += 1
    else:
        right -= 1

print(max_water)