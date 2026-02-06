import sys

liters = int(sys.stdin.readline().strip())

line2 = sys.stdin.readline().strip()
buckets = []
for item in line2.split():
    buckets.append(int(item))

count = 0
for bucket in buckets:
    if liters < bucket or liters <= 0:
        break
    else:
        liters -= bucket
        count += 1
print(count)