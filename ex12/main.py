from pathlib import Path
from collections import defaultdict

move = lambda x, y, dx, dy : (x+dx, y+dy)
h = lambda x, y :move(x, y, 0, 1)
d = lambda x, y :move(x, y, 1, 0)
b = lambda x, y :move(x, y, 0, -1)
g = lambda x, y :move(x, y, -1, 0)

def get_area(specy, pos, area=set()):
    if seen[pos]:
        return area
    seen[pos] = True
    area.add(pos)
    x, y = pos
    dx, dy = 0, 1
    for _ in range(4):
        n = (x+dx, y+dy)
        dx, dy = -dy, dx
       
        if seen[n]:
            continue
        if n in garden and garden[n] == specy:
            area.update(get_area(specy, n,area))
    return area   

def sides(area, specy):
    
    perimeter, size = 0, 0
    for x,y in area:
        cell = x, y
        hcell = h(x, y)
        bcell = b(x, y)
        dcell = d(x, y)
        gcell = g(x, y)
        
        if garden.get(hcell,'') != specy:
            perimeter += 1
            if garden.get(gcell,'') != specy:
                size+=1
            else:
                hgcell = h(*gcell)
                if garden.get(hgcell,'') == specy:
                    size+=1
        
        if garden.get(dcell,'') != specy:
            perimeter += 1
            if garden.get(hcell,'') != specy:
                size+=1
            else:
                dhcell = d(*hcell)
                if garden.get(dhcell,'') == specy:
                    size+=1
        
        if garden.get(bcell,'') != specy:
            perimeter += 1
            if garden.get(gcell,'') != specy:
                size+=1
            else:
                bgcell = b(*gcell)
                if garden.get(bgcell,'') == specy:
                    size+=1
        if garden.get(gcell,'') != specy:
            perimeter += 1
            if garden.get(hcell,'') != specy:
                size+=1
            else:
                ghcell = g(*hcell)
                if garden.get(ghcell,'') == specy:
                    size+=1
            
    return perimeter,size 


garden, species, seen = defaultdict(set), defaultdict(int), defaultdict(bool)
price, price2 = 0, 0

for y,line in enumerate(Path('input.txt').read_text().splitlines()):
    for x,char in enumerate(line):
        garden[(x,y)]=char
        seen[(x,y)]=False
        species[char] += 1

for cell, specy in garden.items():
    if seen[cell]:
        continue
    ar = get_area(specy, cell, set())
    p, s = sides(ar,specy)
    price += p*len(ar)
    price2 += s*len(ar)

print(price)
print(price2)