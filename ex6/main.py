from pathlib import Path

data = Path('input.txt').read_text().splitlines()
total_map = {}

# Init map
for y, line in enumerate(data):
    for x, cell in enumerate(line):
        total_map[(x,y)] = cell
        if cell not in ('.', '#'):
            gard = cell
            gard_pos = (x,y)

# Map solver - return -1 if guard is stuck / solved map if there is a solution
def navigate_map(m, gard, gard_pos, limit):
    exit_reached = False
    gard_moves = {'<':(-1,0),'^':(0,-1),'>':(1,0),'V':(0,1)}
    gard_rotation = list(gard_moves.keys())
    nb_move = 0

    while not exit_reached:
        next_cell = (gard_pos[0]+gard_moves.get(gard)[0], gard_pos[1]+gard_moves.get(gard)[1])
        nb_move += 1
        
        if not 0<=next_cell[0]<len(data) or not 0<=next_cell[1]<len(data[0]):
            exit_reached = True
            m[gard_pos] = f'X{gard}'
            continue
        
        if nb_move > limit or m[next_cell] == f'X{gard}':
            # exits as stuck if limit reached or if in the same path as before (visited in the same direction)
            return -1
        
        if m[next_cell] != '#':
            m[gard_pos] = f'X{gard}'
            m[next_cell] = gard
            gard_pos = next_cell
            continue
            
        current_idx = [i for i,k in enumerate(gard_rotation) if k == gard][0]
        new_idx = current_idx+1 if current_idx<3 else 0
        gard = gard_rotation[new_idx]
    return m

first_map = total_map.copy()

print(sum(1 for cell in navigate_map(first_map, gard, gard_pos,100000).values() if cell.startswith('X')))

good_location = 0
limit = len(data)*len(data)
# Search to stuck the guard by adding obstacle on each step of the path
for pos, cell in total_map.items():
    if not first_map[pos].startswith('X'):
        continue
    second_map = total_map.copy()
    second_map[pos] = '#'
    if navigate_map(second_map, gard, gard_pos,limit) == -1:
        good_location += 1

print(good_location)