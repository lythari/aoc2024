from pathlib import Path
from collections import defaultdict

def get_largest_chain(visited, last):
    for pc in connections[last]:
        if all(v in connections[pc] for v in visited):
            visited.add(pc)
            yield (visited, pc)
            
            
connections, possible_groups_of_3, possible_groups = defaultdict(list), set(), defaultdict(list)

for line in Path('input.txt').read_text().splitlines():
    pc1, pc2 = line.split('-')
    connections[pc1].append(pc2)
    connections[pc2].append(pc1)

for k, v in connections.items():
    if not k.startswith('t'):
        continue
    subset = set()
    for pc in v:
        for pc2 in [pc2 for pc2 in connections[pc] if k in connections[pc2]]:
            subset.add((k,pc,pc2))
    possible_groups_of_3.update([tuple(sorted(team)) for team in subset])
    visited = set([k])
    queue = [(visited, k)]

    while queue:
        visited, pc = queue.pop()
        possible_groups[k].append(visited)
        for v,p in get_largest_chain(visited, pc):
            queue.append((v,p))

longest = ('', 0)
for k, v in possible_groups.items():
    for l in v:
        if len(l) > longest[1]:
            longest = (l, len(l))

print(len(possible_groups_of_3))
print(','.join(sorted([*longest[0]])))