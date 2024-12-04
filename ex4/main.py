from pathlib import Path

data = Path('input.txt').read_text()
lines = data.splitlines()
nb_cols = len(lines[0])
nb_lines = len(lines)

tot = 0

for i in range(nb_lines): 
    for j in range(nb_cols):
        l = lines[i][j]
        if l == 'X': 
            #forward
            if j<=nb_cols-4:
                if lines[i][j:j+4] == 'XMAS':
                    tot += 1
                if i<=nb_lines-4:
                    if lines[i+1][j+1]+lines[i+2][j+2]+lines[i+3][j+3] == 'MAS':
                        tot+=1
                if i>=3:
                    if lines[i-1][j+1]+lines[i-2][j+2]+lines[i-3][j+3] == 'MAS':
                        tot+=1
            if j>=3:
                if lines[i][j-3:j] == 'SAM':
                    tot += 1
                if i<=nb_lines-4:
                    if lines[i+1][j-1]+lines[i+2][j-2]+lines[i+3][j-3] == 'MAS':
                        tot+=1
                if i>=3:
                    if lines[i-1][j-1]+lines[i-2][j-2]+lines[i-3][j-3] == 'MAS':
                        tot+=1
            if i<=nb_lines-4:
                if lines[i+1][j]+lines[i+2][j]+lines[i+3][j] == 'MAS':
                        tot+=1
            if i>=3:
                if lines[i-1][j]+lines[i-2][j]+lines[i-3][j] == 'MAS':
                        tot+=1
print(tot)


tot = 0

for i in range(1,nb_lines-1): 
    for j in range(1,nb_cols-1):
        if lines[i][j] == 'A': 
            if lines[i-1][j-1]+lines[i+1][j+1]+lines[i-1][j+1]+lines[i+1][j-1] in ("SMSM","SMMS","MSMS","MSSM"):
                tot+=1
print(tot)