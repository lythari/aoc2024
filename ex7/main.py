from pathlib import Path


def is_possible(r, l, s= None):
    
    if not l:
        return r in s
    cur = l.pop(0)
    if s is None:
        return is_possible(r, l, (cur, cur, cur))
    if not l:
        return r in (cur + i for i in s) or r in (cur * i for i in s) or r in (int(str(i)+str(cur)) for i in s)

    return is_possible(r, l.copy(), (s[0]+cur, s[0]*cur, int(str(s[0])+str(cur)))) or is_possible(r, l.copy(), (s[1]+cur, s[1]*cur, int(str(s[1])+str(cur)))) or is_possible(r, l.copy(), (s[2]+cur, s[2]*cur, int(str(s[2])+str(cur))))

data = Path('input.txt').read_text().splitlines()
print(sum(int(a) for a,b in (line.split(':') for line in data ) if is_possible(int(a), list(map(int,b.split())))))
