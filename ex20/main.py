from pathlib import Path
from collections import defaultdict, deque

def get_cheats(start_pos, start_val, max_duration):
    x, y = start_pos
    cheats = {}
    for dx in range(max_duration+1):
        for dy in range(max_duration+1):
            if dx+dy > max_duration:
                continue
            new_pos = [(x+dx, y+dy),(x+dx, y-dy), (x-dx, y+dy), (x-dx, y-dy)]
            for np in new_pos:
                if np not in racetrack or not start_val < shortest_race_path[np] < 1000000:
                    continue
                if shortest_race_path[np] - start_val - dx - dy > 99:
                    cheats[(*start_pos,*np)] = shortest_race_path[np] - start_val - dx - dy
    return len(cheats)


racetrack, shortest_race_path, queue = {}, defaultdict(lambda :1000000), deque()
race_direction = [(0,1), (0,-1), (1,0), (-1,0)]

for y, line in enumerate(Path('input.txt').read_text().splitlines()):
    for x, char in enumerate(line):
        if char == 'S' :
            queue.append(((x,y), 0))
        if char != '#':
            racetrack[(x,y)] = '.'

while queue: 
    (x, y), val = queue.pop()
    if val < shortest_race_path[(x, y)]:
        shortest_race_path[(x, y)] = val
    for dx, dy in race_direction:
        if (x+dx, y+dy) in racetrack and shortest_race_path[(x+dx, y+dy)] > val+1:
            queue.append(((x+dx, y+dy),val+1))

cheats_2, cheats_20 = 0, 0
for pos, char in racetrack.items():
    if char != '.':
        continue
    cheats_2 += get_cheats(pos, shortest_race_path[pos], 2)
    cheats_20 += get_cheats(pos, shortest_race_path[pos], 20)


print(cheats_2)
print(cheats_20)