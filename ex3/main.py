from pathlib import Path
from re import compile, findall

data = Path('input.txt').read_text()
pattern = compile(r"mul\((\d{1,3}),(\d{1,3})\)")
total = 0 
enabled = True

for a, b in findall(pattern, data): 
    total += int(a)*int(b)

print(total)

pattern = compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do|don't)\(\)")
total = 0 

for a, b, c in findall(pattern, data): 
    if c:
        enabled = c == "do"
    elif enabled:
        total += int(a)*int(b)

print(total)