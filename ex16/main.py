from pathlib import Path
from collections import defaultdict, deque
from datetime import datetime

def debug(cell, string):
    if not cell:
        print(cell, string)

maze = defaultdict(str)
maze_score = defaultdict(lambda : 1000000)
maze_path = defaultdict(set)
precedence = defaultdict(list)
reverse_direction = {(0,1):(0,-1), (0,-1):(0,1), (1,0):(-1,0), (-1,0):(1,0)}

for y,line in enumerate(Path('input.txt').read_text().splitlines()):
    for x, char in enumerate(line):
        maze[(x,y)]=char
        if char == 'S':
            start = (x,y)
        elif char == 'E':
            end = (x,y)
            maze[end] = '.'
    
direction = (1,0)
queue = deque([(start, direction, 0)])
while queue:
    pos, d, score = queue.popleft()
    if score > 80000:
        continue
    if pos == end:
        maze_score[(pos,d)] = score
        continue
    x, y = pos
    dx, dy = d
    next_cell = x+dx, y+dy
    debug(pos, f"visiting {pos} from {d} with score {score}")
    if maze[next_cell] == '.' and maze_score[(pos,d)] >= score + 1:
        
        maze_score[(pos,d)] = score + 1
        queue.append((next_cell, d, score + 1))
    d1 = dy, -dx
    dx, dy = d1
    
    next_cell = x+dx, y+dy
    d2 = dy, -dx
    dx, dy = d2
    d2 = dy, -dx
    dx, dy = d2
    
    if maze[next_cell] == '.' and maze_score[(pos,d1)]>= score + 1001  :
        maze_score[(pos,d1)] = score + 1001
        queue.append((next_cell, d1, score + 1001))
    next_cell = x+dx, y+dy
    if maze[next_cell] == '.' and maze_score[(pos,d2)]>= score + 1001 :
        debug(pos, f"can turn {d2} : {score+1001} or {maze_score[(pos,d2)]}")
        maze_score[(pos,d2)] = score + 1001
        queue.append((next_cell, d2, score + 1001))

        
score = 1000000
paths = set()
for k, v in maze_score.items():
    cell, d = k
    if cell != end:
        continue
    if v < score:
        score = v
        rev_dir = d
print(score)
dx, dy = reverse_direction[rev_dir]


seen = set()
seen.add(end)
x, y = end
next_cell = x + dx, y + dy

rqueue = deque([(next_cell, reverse_direction[rev_dir], score-1)])

while rqueue:
    a = rqueue.popleft()
    pos, d, score = a
    x, y = pos
    dx, dy = d
    next_cell = x+dx, y+dy
    d1 = -dy, dx
    dx, dy = d1
    next_cell1 = x+dx, y+dy
    d2 = -dy, dx
    dx, dy = d2
    d2 = -dy, dx
    dx, dy = d2
    next_cell2 = x+dx, y+dy
    if maze_score[(next_cell,reverse_direction[d])] == score:
        seen.add(pos)
        rqueue.append((next_cell, d, score-1))
    if maze_score[(next_cell1,reverse_direction[d1])] == score-1000:
        seen.add(pos)
        rqueue.append((next_cell1, d1, score-1001))
    if maze_score[(next_cell2,reverse_direction[d2])] == score-1000:
        seen.add(pos)
        rqueue.append((next_cell2, d2, score-1001))

print(len(set(seen))+1)