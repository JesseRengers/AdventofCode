D = open("inputs/input-1.txt").read().strip()
lines = D.split('\n')
safe_reports = 0

def level_safe(level):
    # Initiality we think the report is safe
    safe = True

    # Determine if the start of the sequence is increasing (1) or decreasing (-1) 
    mode = 1 if int(level[0]) < int(level[1]) else -1

    prev = None
    for num in level:
        cur = int(num)
        # Only go on if prev is set, so once we are at the second number
        if prev:
            step_size = abs(cur - prev)

            # Check all failing cases:
            if step_size < 1 or step_size > 3:
                safe = False
            elif prev < cur and mode == -1:
                safe = False
            elif prev > cur and mode == 1:
                safe = False
        prev = cur
    return safe

# Brute force by splitting up the lines and checking
for line in lines:
        level = list(map(int, line.split()))

        safe = False
        for i in range(len(level)):
            parted = level[:i] + level[i+1:]
            if level_safe(parted):
                safe = True
        if safe:
            safe_reports += 1
print(safe_reports)