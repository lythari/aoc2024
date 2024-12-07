from pathlib import Path
from operator import mul, add

concat = lambda a,b: int(str(a)+str(b))

def is_possible(r, l, ops, s):
    if not l:
        return r in s
    return any(is_possible(r, l[1:], ops, [op(i, l[0]) for op in ops]) for i in s)

def sum_list(data, ops):
    for line in data:
        a,b = line.split(':')
        a = int(a)
        b = list(map(int,b.split()))
        if is_possible(a, b[1:], ops, [b[0] for _ in ops]):
            yield a

data = Path('input.txt').read_text().splitlines()

print(sum(sum_list(data, [add, mul])))
print(sum(sum_list(data, [add, mul, concat])))