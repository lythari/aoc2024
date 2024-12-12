from pathlib import Path
from collections import defaultdict
from math import sqrt
from datetime import datetime 

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

def diag(a, b):
    x1, y1 = a
    x2, y2 = b
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    
def perimeter(area):
    perimeter = 0
    for cell in area:
        x, y = cell
        dx, dy = 0, 1
        for a in range(4):
            n = (x+dx, y+dy)
            dx, dy = -dy, dx
            if n not in area:
                perimeter += 1
    return perimeter
    
def sides(area, specy):
    hdx, hdy = 0, 1
    ddx, ddy = 1, 0
    bdx, bdy = 0, -1
    gdx, gdy = -1, 0
    h, d, b, g = 0, 0, 0, 0
    for y in range(len(data)):
        for x in range(len(data)):
            cell = x, y
            hcell = x+hdx, y+hdy
            bcell = x+bdx, y+bdy
            dcell = x+ddx, y+ddy
            gcell = x+gdx, y+gdy
            
            
            if cell not in area:
                continue
            if garden.get(hcell,'') != specy:
                if garden.get(gcell,'') != specy:
                    h+=1
                else:
                    hgcell = gcell[0]+hdx, gcell[1]+hdy
                    if garden.get(hgcell,'') == specy:
                        h+=1
            
            if garden.get(dcell,'') != specy:
                if garden.get(hcell,'') != specy:
                    d+=1
                else:
                    dhcell = hcell[0]+ddx, hcell[1]+ddy
                    if garden.get(dhcell,'') == specy:
                        d+=1
            
            if garden.get(bcell,'') != specy:
                if garden.get(gcell,'') != specy:
                    b+=1
                else:
                    bgcell = gcell[0]+bdx, gcell[1]+bdy
                    if garden.get(bgcell,'') == specy:
                        b+=1
            if garden.get(gcell,'') != specy:
                if garden.get(hcell,'') != specy:
                    g+=1
                else:
                    ghcell = hcell[0]+gdx, hcell[1]+gdy
                    if garden.get(ghcell,'') == specy:
                        g+=1
            
    return h+d+b+g  


now = datetime.now
garden, species, seen = defaultdict(set), defaultdict(int), defaultdict(bool)

print(now())
data = Path('input.txt').read_text().splitlines()
for y,line in enumerate(data):
    for x,char in enumerate(line):
        garden[(x,y)]=char
        seen[(x,y)]=False
        species[char] += 1


price = 0
price2 = 0



for cell, specy in garden.items():
    if seen[cell]:
        continue
    ar = get_area(specy, cell, set())
    if ar:
        print(cell, specy, len(ar), perimeter(ar), sides(ar,specy)) 
        price += len(ar)*perimeter(ar)
        price2 += len(ar)*sides(ar, specy)


print(price)
print(price2)
