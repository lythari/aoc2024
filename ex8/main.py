from pathlib import Path
from collections import defaultdict
from itertools import combinations


def diagonals(positions):
    x1, y1, x2, y2 = positions
    dx, dy = (x1-x2)/(y1-y2),(y1-y2)/(x1-x2)
    directions = [(1,dy),(-1,-dy),(dx,1),(-dx,-1)]
    for da, db in directions:
        test = x1, y1
        while True:
            x, y = test[0]+da, test[1]+db
            test = x,y
            if not 0<=round(x)<=size[0] or not 0<=round(y)<=size[1]:
                break
            if abs(round(x)-x) > 1/10000 or abs(round(y)-y) > 1/10000:
                continue
            yield int(round(x)),int(round(y))


antenna_map, frequencies, antinodes, resonance = defaultdict(set), set(), set(), set()

for y,line in enumerate(Path('input.txt').read_text().splitlines()):
    for x,char in enumerate(line):
        antenna_map[(x,y)]=char
        if char != '.':
            frequencies.add(char)
size = x,y

for f in frequencies:
    for a, b in combinations([k for k, i in antenna_map.items() if i == f], 2):
        resonance.add(a)
        resonance.add(b)
        x1, y1, x2, y2 = *a, *b
        dx, dy = x1-x2, y1-y2
        antinodes.update((n for n in [(x1+dx,y1+dy), (x2-dx,y2-dy)] if n in antenna_map))
        resonance.update(diagonals((x1,y1,x2,y2)))
print(len(antinodes))
print(len(resonance))