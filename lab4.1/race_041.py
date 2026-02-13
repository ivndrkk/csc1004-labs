import sys

best_runner = None
best_time = None 
best_time_str = ""

for line in sys.stdin:
    parts = line.strip().split()
    name = parts[0]
    times = parts[1:]

    runner_best = None
    valid = True

    for t in times:
        if ':' not in t:
            valid = False
            break

        mins, secs = t.split(':', 1)

        if not mins.isdigit() or not secs.isdigit():
            valid = False
            break

        mins = int(mins)
        secs = int(secs)

        if secs >= 60:
            valid = False
            break

        total = mins * 60 + secs

        if runner_best is None or total < runner_best:
            runner_best = total
            runner_best_str = t

    if not valid:
        continue

    if best_time is None or runner_best < best_time:
        best_time = runner_best
        best_runner = name
        best_time_str = runner_best_str

print(f"{best_runner}: {best_time_str}")
