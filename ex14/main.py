from pathlib import Path
from re import compile, findall
from collections import defaultdict
from time import sleep
 

 
def move(pos, speed, number):
    x, y = pos
    dx, dy = speed
    x = x + number*dx
    y = y + number*dy
    x = x%101
    y = y%103
    space[(x,y)] += 1

def count_space():
    quadrants = [0, 0, 0, 0]
    for i, j in space.items():
        n = 0
        x, y = i
        if x == 50 or y == 51:
            continue
        n = x//51 + 2*(y//52)
        quadrants[n] += j
    
    a, b, c, d = quadrants
    return a*b*c*d
    
def print_space():
    for _ in range(10):
        print()
    for i in range(103):
        for j in range(101):
            print(space.get((j,i),'.'), end='')
        print('')
        
def christmas_tree_pattern_detection():
    for pos, value in space.items():
        if not value:
            continue
        x, y = pos
        tree_pattern = []
        for line in range(1,4): 
            tree_pattern.extend([(x+shift, y+line) for shift in range(1,line+1)])
            tree_pattern.extend([(x-shift, y+line) for shift in range(1,line+1)])
        if all(space.get(p, False) for p in tree_pattern):
            return True
    return False
    
robot_pattern = compile(r"p\=(\d*),(\d*) v\=([-0-9]+),([-0-9]+)")
robots = defaultdict(set)
space = defaultdict(int)


for line in Path('input.txt').read_text().splitlines():
    r = findall(robot_pattern, line)
    x, y, dx, dy = list(map(int,r[0]))
    robots[(x,y)]=(dx, dy)
    move((x,y),(dx,dy),100)


print(count_space())
space = defaultdict(int)

for i in range(85,100001):
    space = defaultdict(int)
    [move(pos,speed,i) for pos, speed in robots.items()]
    if(christmas_tree_pattern_detection()):
        print_space()
        print(i)
        break