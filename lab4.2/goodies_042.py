import sys

all_attendees = None

for line in sys.stdin:
    attendees = set(line.strip().split(","))

    if all_attendees is None:
        all_attendees = attendees
    else:
        all_attendees &= attendees

if not all_attendees:
    print("Uh-oh")
else:
    print(",".join(sorted(all_attendees)))
