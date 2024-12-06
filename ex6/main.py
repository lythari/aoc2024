from pathlib import Path
from datetime import datetime

def navigate_map(b):
    seen, possible_obstacles = {(*start, 0, -1)}, set()
    dx, dy = (0, -1)
    x, y = start
    while True:
        next_cell = (x+dx, y+dy)
        
        if total_map.get(next_cell) is None:
            break
        
        if (*next_cell, dx, dy) in seen:
            # exits if in the same path as before (visited in the same direction)
            return -1

        seen.add((x, y, dx, dy)) 
        if total_map.get(next_cell) and next_cell != b:
            
            if not b and next_cell != start and next_cell not in possible_obstacles:
                if navigate_map(next_cell) == -1:
                    possible_obstacles.add(next_cell)
            x, y = next_cell
            continue
        dx, dy = -dy, dx
    return seen, possible_obstacles

print(datetime.now())
total_map = {}
start = 0, 0

for y, line in enumerate(Path('input.txt').read_text().splitlines()):
    for x, cell in enumerate(line):
        total_map[(x,y)] = False if cell == '#' else True
        if cell not in ('.', '#'):
            start = x, y
visited, test_pos = navigate_map(())

print(len(set((i,j) for i,j,*k in visited)))
print(len(test_pos))
print(datetime.now())
