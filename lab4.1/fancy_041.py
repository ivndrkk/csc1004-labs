import sys

contacts = {}

file = sys.argv[1]
with open(file, 'r') as f:
    for line in f:
        name, phone, email = line.strip().split()
        contacts[name] = {
            "phone" : phone,
            "email" : email
            }
        
for line in sys.stdin:
    name = line.strip()
    if name in contacts:
        print(f'Name: {name}')
        print(f'Phone: {contacts[name]["phone"]}')
        print(f'Email: {contacts[name]["email"]}')
    else:
        print(f'Name: {name}')
        print("No such contact")