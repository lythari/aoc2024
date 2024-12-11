from pathlib import Path
from collections import defaultdict
from textwrap import wrap

global records 
records = defaultdict(set)

def blink_once(stone):
    if (l:=len(str(stone))) % 2 == 0:
        return list(map(int,wrap(str(stone),l//2)))
    return [[stone * 2024], [1]][stone==0]

def blink(stone, nb):
    if (stone, nb) in records:
        return records[(stone, nb)]
    if nb == 1:
        records[(stone, nb)] = len(blink_once(stone))
        return records[(stone, nb)]
    if len(str(stone)) % 2:
        records[(stone, nb)] = [blink(stone*2024, nb - 1), blink(1, nb - 1)][stone==0]
        return records[(stone, nb)]
    return sum(blink(n, nb-1) for n in blink_once(stone))


data = list(map(int, Path('input.txt').read_text().split()))
for turn in [25,75]:
    print(sum(blink(i,turn) for i in data))