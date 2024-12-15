from pathlib import Path
from collections import defaultdict
from datetime import datetime

def sum_area(area):
    return sum([100*p[1]+p[0] for p, v in area.items() if v in ('[','O')])

def exec_steps(user,next_user_cell,area,steps):
    if not steps:
        return user, area
    for pos, char in steps:
        area[pos] = char
    return next_user_cell, area

def horizontal_move(user, area, direction):
    x, y, dx, dy = *user, *direction
    next_user_cell = next_cell = x+dx, y+dy
    steps = [(user,'.'),(next_cell, '@')]
    while True:
        next_char = area[next_cell]
        if next_char == '#':
            return user, area
        if next_char == '.':
            break
        x, y = next_cell
        next_cell = x+dx, y+dy
        steps.append((next_cell, next_char))
    return exec_steps(user, next_user_cell,area,steps)

def vertical_move(user, area, direction):
    x, y, dx, dy = *user, *direction
    next_user_cell = next_cell = x+dx, y+dy
    queue, steps = [], []
    next_char = area[next_cell]
    other_bracket = False 
    if next_char == '#':
        return user, area
    elif next_char == '.':
        steps = [(user,'.'),(next_cell, '@')]
    elif next_char == '[':
        other_bracket = x+dx+1, y+dy
        neigh = x+1, y
    elif next_char == ']':
        other_bracket = x+dx-1, y+dy
        neigh = x-1, y
    else:
        neigh = 0, 0
    queue = [(user,next_cell,'@'), (neigh,other_bracket,'.')] if other_bracket else [(user,next_cell,'@')]

    while queue:
        c, n, char = queue.pop(0)
        if not c in [a for a,b in steps] and c != neigh:
            steps.append([c, '.'])
        r, possible_move = valid_moves(area,(n,char), direction)
        if r:   
            steps.append((n,char))
            queue.extend(possible_move)
        else:
            steps = []
            break
            
    return exec_steps(user, next_user_cell,area,steps)

def valid_moves(area, movement, direction):
    cell, char = movement
    x, y, dx, dy = *cell, *direction
    next_char = area[cell]
    steps = []
    if next_char == '#' or next_char == '':
        return False, []
    if next_char == '.':
        return True, []
    next_cell = x+dx, y+dy
    if next_char == '[':
        other_cell = x+1, y
        other_bracket = x+dx+1, y+dy
    elif next_char == ']':
        other_cell = x-1, y
        other_bracket = x+dx-1, y+dy
    else: 
        return True, [(cell, next_cell, next_char)]
    return True,[(cell,next_cell,next_char),(other_cell,other_bracket,area[other_cell])]


basic_area,real_area,moves = defaultdict(str), defaultdict(str), []
directions = {'^': (0,-1),'<': (-1,0),'>': (1,0),'v': (0,1)}

for y,line in enumerate(Path('input.txt').read_text().splitlines()):
    if line and line[0] in directions:
        moves.extend([directions[char] for char in line.strip()])
    else:
        for x, char in enumerate(line):
            basic_area[(x,y)] = char
            if char == '@':
                basic_user, real_user = (x, y), (2*x,y)
                real_area.update([((2*x,y),'@'),((1+2*x,y),'.')])
            elif char == 'O':
                real_area.update([((2*x,y),'['),((1+2*x,y),']')])
            else:
                real_area.update([((2*x,y),char),((1+2*x,y),char)])

for m in moves:
    basic_user, basic_area= [horizontal_move,vertical_move][m[0]==0](basic_user, basic_area, m)
    real_user, real_area= [horizontal_move,vertical_move][m[0]==0](real_user, real_area, m)

print(sum_area(basic_area))
print(sum_area(real_area))