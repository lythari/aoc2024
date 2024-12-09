from pathlib import Path


checksum = lambda l: (i*j for i,j in enumerate(l) if j != '.')

data = list(map(int, Path('input.txt').read_text()))
disk = []
orig_blocks = {i: j for i,j in enumerate(data[::2])}
orig_spaces = data[1::2]
blocks = orig_blocks.copy()
spaces = orig_spaces.copy()

while spaces:
    char = min(blocks.keys())
    nb = blocks.pop(char)
    disk.extend([char]*nb)
    fill = spaces.pop(0)
    if not blocks:  
        disk.extend(['.']*sum(spaces))
        spaces = []
        break
    while fill:
        char = max(blocks.keys())
        nb = blocks.pop(char)
        if fill<nb:
            disk.extend([char]*fill)
            blocks[char] = nb-fill
            fill = 0
        else:
            disk.extend([char]*nb)
            fill -= nb

print(sum(checksum(disk)))
blocks = orig_blocks.copy()
spaces = orig_spaces.copy()
disk, result, iter_keys = [], [], sorted(blocks.keys(), reverse=True)

while spaces:
    if not blocks:
        disk.append(('.',sum(spaces)))
        spaces = []
        break
    char = min(blocks.keys())
    nb = blocks.pop(char)
    if not nb:
        disk.append(('.',orig_blocks.get(char)))
    else:
        disk.append((char,nb))
    fill = spaces.pop(0)
    for k in sorted(blocks.keys(), reverse=True):
        if not fill:
            break
        nb = blocks.get(k)
        if not nb or fill<nb:
            continue
        else:
            disk.append((k,nb))
            fill -= nb
            blocks[k] = 0
    if fill:
        disk.append(('.',fill))

[result.extend([i]*j) for i,j in disk]
print(sum(checksum(result)))