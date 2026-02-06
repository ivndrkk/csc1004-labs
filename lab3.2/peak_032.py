#!/usr/bin/env python3
import sys

lines = [line.strip() for line in sys.stdin if line.strip()]

grid = [list(map(int, line.split())) for line in lines]

M = len(grid)
N = len(grid[0])

peak = -1

for i in range(1, M - 1):
    for j in range(1, N - 1):
        val = grid[i][j]
        left = grid[i][j - 1]
        right = grid[i][j + 1]
        top = grid[i - 1][j]
        bottom = grid[i + 1][j]
        
        if val > left and val > right and val > top and val > bottom:
            peak = val
            break
    if peak != -1:
        break

print(peak)
