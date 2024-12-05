D = open("input.txt").read().strip()
lines = D.split('\n')

total = 0
rules = {}
good_updates = []
bad_updates = []
# rules is een lijst van alle getallen
# rules[i][0] is een lijst van alle getallen die voor getal i komen
# rules[i][1] is een lijst van alle getallen die na getal i komen
for line in lines:

    # First create the 'rules' hashmap
    if '|' in line:
        i,j = map(int, line.split('|'))
        if not i in rules:
            rules[i] = [[],[]]
            rules[i][0] = []
            rules[i][1] = []
        if not j in rules:
            rules[j] = [[],[]]
            rules[j][0] = []
            rules[j][1] = []
        rules[i][1].append(j)
        rules[j][0].append(i)

    
    if ',' in line:
        update = list(map(int, line.split(',')))
        good_update = True
        for i in range(len(update) -1):
            if i == 0:
            # in this case we don't have a before page
                if update[i] in rules[update[i+1]][1]:
                    good_update = False
            elif i == len(update):
            # in this case we don't have a after page
                if update[i] in rules[update[i-1]][0]:
                    good_update = False
            else:
            # hier zitten we er tussenin
                if update[i] in rules[update[i+1]][1] or update[i] in rules[update[i-1]][0]:
                    #print(f"fout bij update {update}: {update[i]}")
                    good_update = False
        if good_update:
            good_updates.append(update)
        else:
            bad_updates.append(update)

for update in good_updates:
    middle_index = update[len(update) // 2]
    total += middle_index

print(total)