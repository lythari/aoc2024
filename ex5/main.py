from pathlib import Path
from functools import reduce, cmp_to_key
from collections import defaultdict

orders, updates = defaultdict(set), []

def is_ordered_list(my_list,previous_numbers):
    return all(
        not any(j in previous_numbers.get(n) for j in my_list[i:]) 
        for i,n in enumerate(my_list,1))


for line in Path('input.txt').read_text().splitlines(): 
    if '|' in line:
        a, b = map(int,line.split('|'))
        orders[b].add(a)
    elif line:
        updates.append(list(map(int,line.split(','))))

correct_list = [upd for upd in updates if is_ordered_list(upd, orders)]
incorrect_list = [upd for upd in updates if not is_ordered_list(upd, orders)]
corrected_list = [sorted(l, 
                    key=cmp_to_key(lambda a,b: -1 if is_ordered_list([a,b], orders) else 1)) 
                    for l in incorrect_list]

print(reduce(lambda a, b: a + b[len(b)//2], correct_list,0))
print(reduce(lambda a, b: a + b[len(b)//2], corrected_list,0))