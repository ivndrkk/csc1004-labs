import sys

contacts = {}

file = sys.argv[1]
with open(file, 'r') as f:
    for line in f:
        k, v = line.strip().split()
        contacts[k] = v

for line in sys.stdin:
    name = line.strip()
    if name in contacts:
        print(f'Name: {name}')
        print(f'Phone: {contacts[name]}')
    else:
        print(f'Name: {name}')
        print("No such contact")