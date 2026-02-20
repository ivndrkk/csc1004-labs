import sys

grid = [line.strip() for line in sys.stdin if line.strip()]

rows = len(grid)
cols = len(grid[0])

result = ""

for c in range(cols):
    for r in range(rows):
        if grid[r][c] != ".":
            result += grid[r][c]
            break

print(result)