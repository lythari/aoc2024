from pathlib import Path
from collections import defaultdict
from itertools import combinations
from math import ceil, floor

data = Path('input.txt').read_text().splitlines()

antenna_map = defaultdict(set)
frequencies = set()

for y,line in enumerate(data):
    for x,char in enumerate(line):
        antenna_map[(x,y)]=char
        if char != '.':
            frequencies.add(char)
        
size = x,y
antinodes = set()

def diagonals(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    dy = (y1-y2)/(x1-x2)
    test = x1, y1
    while True:
        x = test[0]+1
        y = test[1]+dy
        if not 0<=x<=size[0] or not 0<=round(y)<=size[1]:
            break
        if abs(round(y)-y) > 1/10000:
            test = x,y
            continue
        yield x,int(round(y))
        test = x,y
        
   
    test = x1, y1
    while True:
        x = test[0]-1
        y = test[1]-dy
        if not 0<=x<=size[0] or not 0<=round(y)<=size[1]:
            break
        if abs(round(y)-y) > 1/10000:
            test = x,y
            continue
        yield x,int(round(y))
        test = x,y
            
    dx = (x1-x2)/(y1-y2)
    test = x1, y1
    while True:
        x = test[0]+dx
        y = test[1]+1
        print(x,y)
        if not 0<=round(x)<=size[0] or not 0<=y<=size[1]:
            break
        if abs(round(x)-x) > 1/10000:
            test = x,y
            continue
        yield int(round(x)),y
        test = x,y
   
    test = x1, y1
    while True:
        x = test[0]-dx
        y = test[1]-1
        print(x,y)
        if not 0<=round(x)<=size[0] or not 0<=y<=size[1]:
            break
        if abs(round(x)-x) > 1/10000:
            test = x,y
            continue
        yield int(round(x)),y
        test = x,y

for f in frequencies:
    print(f)
    for a, b in combinations([k for k, i in antenna_map.items() if i == f], 2):
        antinodes.add(a)
        antinodes.add(b)
        x1, y1, x2, y2 = *a, *b
        
        for node in diagonals((x1,y1),(x2,y2)):
            antinodes.add(node)

print(sorted(antinodes))
print(len(antinodes))