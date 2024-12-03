import re

D = open("inputs/test.txt").read().strip()
lines = D.split('\n')

mul_re = "mul\(\d{1,3},\d{1,3}\)"

total = 0

for line in lines:
    to_be_multiplied = re.findall(mul_re,line)
    for item in to_be_multiplied:
        x,y = item.strip("xmul()").split(',')
        total += int(x) * int(y)

print(total)