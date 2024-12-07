D = open("input.txt").read().strip()
lines = D.split('\n')

from itertools import product
answer = 0
for line in lines:
    # remove the : and make a list of ints
    line = list(map(int,line.replace(':','').split(' ')))
    total = line[0]
    numbers = line[1:]
    
    for combo in product('+*|', repeat=len(numbers) -1):
        print(combo)
        subtotal = numbers[0]
        for i in range(1, len(numbers)):
            if combo[i-1] == "+":
                subtotal += numbers[i]
            elif combo[i-1] == "*":
                subtotal *= numbers[i]
            else:
                subtotal = int(str(subtotal) + str(numbers[i]))
        if subtotal == total:
            answer += total
            break

print(answer)
