import sys

def uniqueNum(num_str):
    seen = {}
    nums_list = num_str.split()
    for i in range(len(nums_list)):
        if nums_list[i] not in seen:
            seen[nums_list[i]] = 1
        else:
            seen[nums_list[i]] += 1
            
    result = "none"
    for key, value in seen.items():
        if value == 1 and int(key) > (int(result) if result != "none" else -1):
            result = key
    return result

for line in sys.stdin:
    line = line.strip()
    print(uniqueNum(line))