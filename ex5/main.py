from pathlib import Path
from functools import reduce

def read_input(data):
    lines = data.splitlines()
    orders = {}
    updates = []
    step1 = True

    for line in lines: 
        if not line:
            step1 = False
            continue
        if step1:
            a, b = line.split('|')
            orders[int(b)] = orders.get(int(b),[]) + [int(a)]
        else:
            updates.append(list(map(int,line.split(','))))
    return orders, updates

def sum_middle_number(my_lists): 
    return reduce(lambda a, b: a + b[len(b)//2], [0]+list(my_lists))

def is_ordered_list(my_list,previous_numbers):
    return all(
        all(n in previous_numbers.get(j, []) for j in my_list[i:])
        for i,n in enumerate(my_list,1)
    )
    
def order_a_list(my_list, previous_numbers):
    new_list = []
    while my_list:
        for i, j in enumerate(my_list):
            if not any(j in previous_numbers.get(n, []) for n in my_list if n!=j):
                del my_list[i]
                new_list.append(j)
                break
    return new_list[::-1]


data = Path('input.txt').read_text()
orders, updates = read_input(data)
correct_list = [upd for upd in updates if is_ordered_list(upd, orders)]
incorrect_list = [upd for upd in updates if not is_ordered_list(upd, orders)]
corrected_list = [order_a_list(l, orders) for l in incorrect_list]

print(sum_middle_number(correct_list))
print(sum_middle_number(corrected_list))