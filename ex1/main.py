from pathlib import Path
from collections import Counter


def read_file(long_str):
    list1 = []
    list2 = []

    for line in long_str.splitlines():
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))

    return sorted(list1), sorted(list2)


list1, list2 = read_file(Path('input.txt').read_text())
c = Counter(list2)

print(sum(abs(a-b) for a,b in zip(list1, list2)))
print(sum(a*c.get(a, 0) for a in list1))