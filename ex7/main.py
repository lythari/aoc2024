from pathlib import Path
from operator import mul, add

concat = lambda a,b: int(str(a)+str(b))

def is_possible(r, l, ops, s= None):
    if not l:
        return r in s
    cur = l[0]
    if s is None:
        return is_possible(r, l[1:], ops, [cur for _ in ops])
    if len(l) == 1:
        return any(op(i,cur) == r for i in s for op in ops)
    return any(is_possible(r, l[1:], ops, [op(i, cur) for op in ops]) for i in s)

data = Path('input.txt').read_text().splitlines()
print(sum(int(a) for a,b in (line.split(':') for line in data ) if is_possible(int(a), list(map(int,b.split())), [add, mul])))
print(sum(int(a) for a,b in (line.split(':') for line in data ) if is_possible(int(a), list(map(int,b.split())), [add, mul, concat])))
