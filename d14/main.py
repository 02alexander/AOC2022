#!/usr/bin/env python3

import sys
import numpy as np
lines = sys.stdin.readlines()

paths = []
minx = 100000000
maxx = -10000000
miny = 100000000
maxy = -1000000
for line in lines:
    path = []
    for point in line.split('->'):
        x, y = eval(f'({point})')
        minx = min(x, minx)
        maxx = max(x, maxx)
        miny = min(y, miny)
        maxy = max(y, maxy)

        path.append((x, y))
    paths.append(path)

print(minx, maxx)
print(miny, maxy)

structure = np.zeros((maxy+3, maxx-minx+2*(maxy)))

rows, cols = np.shape(structure)
for c in range(cols):
    structure[-1, c] = 1

miny = miny-1
minx = minx-maxy
print(f'structure=\n{structure}')

for path  in paths:
    curx, cury = path[0]
    structure[cury, curx-minx] = 1
    for i in range(1, len(path)):
        x, y = path[i]
        while x != curx or y != cury:
            dx = max(-1, min(1, -curx+x))
            dy = max(-1, min(1, -cury+y))
            curx = curx+dx
            cury = cury+dy
            structure[cury, curx-minx] = 1
        structure[cury, curx-minx] = 1

print(f'structure=\n{structure}')

cnt = 0
is_done = False
while True and not is_done:
    curx, cury = (500, 0)
    cnt += 1
    while True:
        if cury+1 >= rows:
            is_done = True
            print("ERROR"*10)
            break

        if structure[cury+1, curx-minx] == 0:
            cury = cury+1
        elif structure[cury+1, curx-1-minx] == 0:
            cury = cury+1
            curx = curx-1
        elif structure[cury+1, curx+1-minx] == 0:
            cury = cury+1
            curx = curx+1
        else:
            break

    if (curx, cury) == (500,0):
        break
    if not is_done:
        structure[cury, curx-minx] = 2
    

print(cnt)
    
