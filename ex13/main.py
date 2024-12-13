from pathlib import Path
from re import compile, findall
 
def move(buttons, target):
    ax, ay = buttons['A']
    bx, by = buttons['B']
    x, y = target
    m1,m2 = (x*ay-y*ax), (by*ax-bx*ay)
    n1,n2 = (x*by-y*bx), (bx*ay-by*ax)
    if m1%m2 or n1%n2:
        return 0
    return 1*abs(m1//m2) + 3*abs(n1//n2)
    
pattern_button = compile(r"Button ([A-B]): X\+(\d+), Y\+(\d+)")
pattern_prize = compile(r"Prize: X\=(\d+), Y\=(\d+)")
token1, token2, buttons = 0, 0, {}

for line in Path('input.txt').read_text().splitlines():
    if line.startswith("Bu"):
        l, x, y = findall(pattern_button, line)[0]
        buttons[l] = (int(x),int(y))
    elif line:
        x, y = findall(pattern_prize, line)[0]
        token1 += move(buttons, (int(x),int(y)))
        token2 += move(buttons, (10000000000000+int(x),10000000000000+int(y)))

print(token1)
print(token2)