from pathlib import Path
from collections import defaultdict
from datetime import datetime

def walk(pos, n=1):
    x, y = pos
    dx, dy = 0, 1
    good_path = []
    for i in range(4):
        p = x+dx,y+dy
        if data[p] == n:
            good_path.append(p)
        dx, dy = -dy, dx
    if n == 9:
        return good_path
    sub_path = []
    [sub_path.extend(walk(p,n+1)) for p in good_path]
    return sub_path
    
data, starts, results, unique_results = defaultdict(tuple), set(), [], []

for l, line in enumerate(Path('input.txt').read_text().splitlines()):
    for c, val in enumerate(line):
        data[(c,l)] = int(val)
        if val == '0':
            starts.add((c,l))

[unique_results.extend(set(walk(p))) for p in starts]
[results.extend(walk(p)) for p in starts]
print(len(unique_results))
print(len(results))

