from pathlib import Path
from itertools import pairwise, product
from functools import cache
import re

@cache
def possible_num_moves(from_button, to_button):
    s = numpad_keys[from_button]
    t = numpad_keys[to_button]
    sx, sy = s
    tx, ty = t
    
    hf = abs(sx-tx)*moves[[(-1,0),(1,0)][tx>sx]]+ abs(sy-ty)*moves[[(0,-1),(0,1)][ty>sy]] + 'A'
    vf = abs(sy-ty)*moves[[(0,-1),(0,1)][ty>sy]]+ abs(sx-tx)*moves[[(-1,0),(1,0)][tx>sx]] + 'A'
    
    if ty==3 and sx == 0: 
        return [hf]
    if tx == 0 and sy == 3:
        return [vf]
    return [hf,vf]

@cache
def shortest_arrow_move(from_button, to_button, iterations):
    s = arrow_keys[from_button]
    t = arrow_keys[to_button]
    sx, sy = s
    tx, ty = t
    if iterations == 0:
        return abs(sx-tx)+abs(sy-ty)+1
    
    
    hf = 'A' +abs(sx-tx)*moves[[(-1,0),(1,0)][tx>sx]]+ abs(sy-ty)*moves[[(0,-1),(0,1)][ty>sy]] + 'A'
    vf = 'A' +abs(sy-ty)*moves[[(0,-1),(0,1)][ty>sy]]+ abs(sx-tx)*moves[[(-1,0),(1,0)][tx>sx]] + 'A'
    
    
    hc = sum(shortest_arrow_move(hf[x], hf[x+1], iterations-1) for x in range(len(hf)-1))
    vc = sum(shortest_arrow_move(vf[x], vf[x+1], iterations-1) for x in range(len(vf)-1))
    
    if ty==0 and sx == 0: 
        return hc
    if tx == 0 and sy == 0:
        return vc
    return min(hc, vc)


pattern = re.compile('(\d+)A')
arrow_keys = {'A' : (2,0), '^': (1,0), '<': (0,1), 'v': (1,1), '>': (2,1)}
numpad_keys = {'7': (0,0), '8':(1,0), '9':(2,0),'4': (0,1), '5':(1,1), '6':(2,1),'1':(0,2),'2':(1,2),'3':(2,2),'0':(1,3),'A':(2,3)}
moves = {(0,1): 'v', (1,0): '>', (0,-1): '^', (-1,0):'<'}
tot_2 = tot_25 = tot_100 = 0

for code in Path('input.txt').read_text().splitlines():
    l2 = l25 = l100 = float('inf')
    num = int(pattern.search(code).groups()[0])
    sub_sequences = product(*[possible_num_moves(pos,target) for pos, target in pairwise('A'+code)])
    digit_sequences = set(['A'+''.join(s) for s in sub_sequences])
    
    for instructions in digit_sequences:
        m2 = sum(shortest_arrow_move(instructions[x], instructions[x+1], 1) for x in range(len(instructions)-1))
        m25 = sum(shortest_arrow_move(instructions[x], instructions[x+1],24) for x in range(len(instructions)-1))
        m100 = sum(shortest_arrow_move(instructions[x], instructions[x+1],99) for x in range(len(instructions)-1))
        l2 = min(m2,l2)
        l25 = min(m25,l25)
        l100 = min(m100,l100)
    
    tot_2 += num*l2
    tot_25 += num*l25
    tot_100 += num*l100

print(tot_2,tot_25, tot_100)