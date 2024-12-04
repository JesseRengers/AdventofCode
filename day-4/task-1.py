import re

D = open("inputs/test.txt").read().strip()
lines = D.split('\n')

matrix = []
for line in lines:
    matrix.append(list(line))

# Direction can be
# horizontal_right, horizontal_left, 
# vertical_up, vertical_down, 
# diagonal_1 (left->right, up), diagonal_2 (right->left, up)
# diagonal_3 (left->right, down), diagonal_4 (right->left, down)

XMAS = ['X','M','A','S']

def search_xmas(i,j,letter,direction,matrix):
    if i < 0 or j < 0:
        return
    if letter == len(XMAS) -1:
        print(f"we have found a {direction} ending at {i,j}")
    else:
        try:
            if direction == "horizontal_right":
                if matrix[i][j+1] == XMAS[letter+1]:
                    search_xmas(i,j+1,letter+1,"horizontal_right",matrix)
            elif direction == "horizontal_left":
                if matrix[i][j-1] == XMAS[letter+1]:
                    search_xmas(i,j-1,letter+1,"horizontal_left",matrix)
            elif direction == "vertical_up":
                if matrix[i+1][j] == XMAS[letter+1]:
                    search_xmas(i+1,j,letter+1,"vertical_up",matrix)
            elif direction == "vertical_down":
                if matrix[i-1][j] == XMAS[letter+1]:
                    search_xmas(i-1,j,letter+1,"vertical_down",matrix)
            elif direction == "diagonal_1":
                if matrix[i+1][j+1] == XMAS[letter+1]:
                    search_xmas(i+1,j+1,letter+1,"diagonal_1",matrix)
            elif direction == "diagonal_2":
                if matrix[i+1][j-1] == XMAS[letter+1]:
                    search_xmas(i+1,j-1,letter+1,"diagonal_2",matrix)
            elif direction == "diagonal_3":
                if matrix[i-1][j+1] == XMAS[letter+1]:
                    search_xmas(i-1,j+1,letter+1,"diagonal_3",matrix)
            elif direction == "diagonal_4":
                if matrix[i-1][j-1] == XMAS[letter+1]:
                    search_xmas(i-1,j-1,letter+1,"diagonal_4",matrix)
            else:
                # Try all
                try: 
                    if matrix[i][j+1] == XMAS[letter+1]:
                        search_xmas(i,j+1,letter+1,"horizontal_right",matrix)
                except IndexError:
                    pass
                try:
                    if matrix[i][j-1] == XMAS[letter+1]:
                        search_xmas(i,j-1,letter+1,"horizontal_left",matrix)
                except IndexError:
                    pass
                try:
                    if matrix[i+1][j] == XMAS[letter+1]:
                        search_xmas(i+1,j,letter+1,"vertical_up",matrix)
                except IndexError:
                    pass
                try:
                    if matrix[i-1][j] == XMAS[letter+1]:
                        search_xmas(i-1,j,letter+1,"vertical_down",matrix)
                except IndexError:
                    pass
                try:
                    if matrix[i+1][j+1] == XMAS[letter+1]:
                        search_xmas(i+1,j+1,letter+1,"diagonal_1",matrix)
                except IndexError:
                    pass
                try:
                    if matrix[i+1][j-1] == XMAS[letter+1]:
                        search_xmas(i+1,j-1,letter+1,"diagonal_2",matrix)
                except IndexError:
                    pass
                try:
                    if matrix[i-1][j+1] == XMAS[letter+1]:
                        search_xmas(i-1,j+1,letter+1,"diagonal_3",matrix)
                except IndexError:
                    pass
                try:
                    if matrix[i-1][j-1] == XMAS[letter+1]:
                        search_xmas(i-1,j-1,letter+1,"diagonal_4",matrix)
                except IndexError:
                    pass
        except IndexError:
            pass

        
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'X':
            search_xmas(i,j,0,'unknown',matrix)

# to find the total: python3 task-1.py | wc -l