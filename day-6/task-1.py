import sys
sys.setrecursionlimit(14500)

D = open("input.txt").read().strip()
grid = D.split('\n')
visited = set()

# we turn clockwise
directions = ["UP", "RIGHT", "DOWN", "LEFT"]

# create the grid
for i in range(len(grid)):
    grid[i] = list(grid[i])



# find starting position
for i in range(len(grid) -1):
    for j in range(len(grid[i]) -1):
        if grid[i][j] == "^":
            pos = (j,i)
            visited.add((j,i))

# returns True if an obstacle is on x,y
def is_obstacle(x,y) -> bool:
    if out_of_grid(x,y):
        return False
    return grid[y][x] == "#"

# returns True if x,y is off grid
def out_of_grid(x,y) -> bool:
    if x < 0 or y < 0:
        return True
    
    height = len(grid)
    width = len(grid[0])
    
    if y >= height or x >= width:
        return True
    return False

# input: waar we staan en welke directie we op willen
# output: waar we terecht komen en welke directie daar bij hoort
def turn(x,y,dir):
    if dir == 0 and not is_obstacle(x+1,y):
        return x+1,y,1
    elif dir == 1 and not is_obstacle(x,y+1):
        return x,y+1,2
    elif dir == 2 and not is_obstacle(x-1,y):
        return x-1,y,3
    elif dir == 3 and not is_obstacle(x,y-1):
        return x,y-1,0
    else:
        return turn(x,y,dir + (1 % 4))

def walk(x,y,dir):
    if dir == 0 and not is_obstacle(x,y-1):
        if out_of_grid(x,y-1):
            return
        visited.add((x,y-1))
        return walk(x,y-1,0)
    if dir == 1 and not is_obstacle(x+1,y):
        if out_of_grid(x+1,y):
            return
        visited.add((x+1,y))
        return walk(x+1,y,1)
    if dir == 2 and not is_obstacle(x,y+1):
        if out_of_grid(x,y+1):
            return
        visited.add((x,y+1))
        return walk(x,y+1,2)
    if dir == 3 and not is_obstacle(x-1,y):
        if out_of_grid(x-1,y):
            return
        visited.add((x-1,y))
        return walk(x-1,y,3)
    new_x,new_y,new_dir = turn(x,y,dir)
    if out_of_grid(new_x,new_y):
        return
    visited.add((new_x,new_y))
    walk(new_x,new_y,new_dir)
    
walk(pos[0],pos[1],0)
print(len(visited))