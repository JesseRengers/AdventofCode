import re

D = open("inputs/input.txt").read().strip()
lines = D.split('\n')

total = 0
matrix = []
for line in lines:
    matrix.append(list(line))

def search_xmas(i,j):

    try:
        upper_left = matrix[i-1][j-1]
        upper_right = matrix[i-1][j+1]
        lower_left = matrix[i+1][j-1]
        lower_right = matrix[i+1][j+1]
    except IndexError:
        return False
  
    if upper_left == 'M':
        if upper_right == 'S':
            if (lower_left == 'M' and lower_right == 'S'):
                return True
        elif upper_right == 'M' and lower_right == 'S' and lower_left == 'S':
            return True
    elif upper_left == 'S':
        if upper_right == 'M':
            if (lower_left == 'S' and lower_right == 'M'):
                return True
        elif upper_right == 'S' and lower_right == 'M' and lower_left == 'M':
            return True

    return False
    

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'A':
            if search_xmas(i,j):
                total+= 1
print(total)