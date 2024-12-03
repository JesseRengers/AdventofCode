import re

D = open("inputs/test.txt").read().strip()
lines = D.split('\n')

mul_re = "mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"

total = 0
do = True
for line in lines:
    regex_result = re.findall(mul_re,line)
    for item in regex_result:
        if item == "don't()":
            do = False
        elif item == "do()":
            do = True
        elif do:
            x,y = item.strip("xmul()").split(',')
            total += int(x) * int(y)

print(total)