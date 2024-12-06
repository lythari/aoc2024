from pathlib import Path
from datetime import datetime


def navigate_map(m, gard, gard_pos, real=False):
    exit_reached = False
    gard_moves = {'<':(-1,0),'^':(0,-1),'>':(1,0),'V':(0,1)}
    gard_rotation = list(gard_moves.keys())
    nb_move = 0
    seen = set()
    possible_obstacles = set()
    current_idx = 1
    size = max(list(m.keys()))
    while not exit_reached:
        next_cell = (gard_pos[0]+gard_moves.get(gard)[0], gard_pos[1]+gard_moves.get(gard)[1])
        nb_move += 1
        seen.add(gard_pos)
        if not 0<=next_cell[0]<=size[0] or not 0<=next_cell[1]<=size[1]:
            exit_reached = True
            m[gard_pos] = f'X{gard}'
            continue
        
        if nb_move > size[0]*size[1]/2 or m[next_cell] == f'X{gard}':
            # exits as stuck if limit reached or if in the same path as before (visited in the same direction)
            return -1
            
        if m[next_cell] != '#':
            if real and next_cell not in possible_obstacles:
                orthogonal_obstacles = 0
                match current_idx:
                    case 0:
                        orthogonal_obstacles = columns[gard_pos[1]][:gard_pos[0]].count('#')
                    case 1:
                        orthogonal_obstacles =  lines[gard_pos[0]][:gard_pos[1]].count('#')
                    case 2:
                        orthogonal_obstacles =  columns[gard_pos[1]][gard_pos[0]:].count('#')
                    case 3:
                        orthogonal_obstacles =  lines[gard_pos[0]][gard_pos[1]:].count('#')
                    case _:
                        orthogonal_obstacles = 0
                if orthogonal_obstacles and navigate_map(m.copy() | {next_cell: '#'}, gard, gard_pos) == -1:
                    possible_obstacles.add(next_cell)

            m[gard_pos] = f'X{gard}'
            m[next_cell] = gard
            gard_pos = next_cell
            continue
        new_idx = current_idx+1 if current_idx<3 else 0
        current_idx = new_idx
        gard = gard_rotation[new_idx]
    return seen, possible_obstacles

print(datetime.now())
lines = Path('input.txt').read_text().splitlines()
columns = [''.join(i) for i in zip(*lines)]

total_map = {}

for y, line in enumerate(lines):
    for x, cell in enumerate(line):
        total_map[(x,y)] = cell
        if cell not in ('.', '#'):
            gard = cell
            gard_pos = (x,y)
init_gard = gard_pos
visited, test_pos = navigate_map(total_map.copy(), gard, gard_pos,True)
test_pos.add(init_gard)
test_pos.remove(init_gard)
print(len(visited))
print(len(test_pos))
print(datetime.now())
