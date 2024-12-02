safe_reports = 0

with open("inputs/input-1.txt") as file:
    for line in file:
        line = line.split()

        # Initiality we think the report is safe
        safe = True

        # Determine if the start of the sequence is increasing (1) or decreasing (-1) 
        mode = 1 if int(line[0]) < int(line[1]) else -1

        prev = None
        for num in line:
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
        
        safe_reports = safe_reports + 1 if safe else safe_reports
    
print(safe_reports)