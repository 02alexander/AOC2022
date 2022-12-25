#!/usr/bin/env python3

import sys
import re
import numpy as np

data = sys.stdin.read()

fh, lh  = data.split('\n\n')

lines = fh.splitlines()
rows = len(lines)
cols = max(len(line) for line in lines)
mp = np.zeros((rows+2, cols+2))

visited = dict()

start = None
for r, line in enumerate([" "*(cols+2)]+lines+[" "*(cols+2)]): # [" "*(cols+2)]+lines+[" "*(cols+2)]
    for c, ch in enumerate(" "+line.rstrip()+" "):
        if ch == '.':
            if start is None:
                start = c+1j*r
            mp[r, c] = 2
        elif ch == '#':
            mp[r,c] = 1

cur = None
instructions = []
for ch in lh.strip():
    if ch.isalpha():
        if cur:
            instructions.append(int(cur))
            cur = None
        instructions.append(ch)
    else:
        if cur is None:
            cur = ""
        cur += ch

def drtoch(dr):
    if dr == 1:
        return ('>')
    elif dr == -1:
        return ('<')
    elif dr == 1j:
        return ('v')
    elif dr == -1j:
        return ('^')
    else:
        print(f"error on {dr}")
        sys.exit()

def pretty_print(mp, cur=None):
    rows, cols = np.shape(mp)
    for row in range(rows):
        for col in range(cols):
            if cur:
                if col == int(cur.real) and row == int(cur.imag):
                    print('A', end="")
                    continue
            if (col+1j*row) in visited:

                print(visited[col+1j*row], end="")
                continue
            if mp[row,col] == 0:
                print(' ', end="")
            if mp[row,col] == 1:
                print('#', end="")
            if mp[row,col] == 2:
                print('.', end="")

        print()


rows, cols = np.shape(mp)
ver_changes = set()
hor_changes = set()
for row in range(rows):
    for col in range(cols-1):
        if ( mp[row, col] == 0 or mp[row, col+1] == 0 )and mp[row,col] != mp[row,col+1]:
            hor_changes.add(col)

for col in range(cols):
    for row in range(rows-1):
        if ( mp[row, col] == 0 or mp[row+1, col] == 0 ) and mp[row,col] != mp[row+1,col]:
            ver_changes.add(row)

print(f'ver_changes={ver_changes}')
print(f'hor_changes={hor_changes}')

# side_mappings = {
#     #((9,0), (13, 0), (-1j)): ((0, 5), (0,9), (1j)),
#     ((5, 13), (8, 13), (1)): ((8, 16), (8, 13), (1j)),
#     ((13, 9), (13, 12), (1j)): ((9, 4), (9, 1), (-1j)),
#     ((4, 5), (4, 8), (-1j)): ((1, 8), (4, 8), (1)),
#     #((5, 5), (9, 5), (-1j)): (())

# }

side_mappings = {
    ((0, 51), (0, 100), (-1j)): ((151, 0), (200, 0), (1)), # checked
    ((201, 1), (201, 50), (1j)): ((0, 101), (0, 150), (1j)), # checked
    ((151, 51), (200, 51), (1)): ((151, 51), (151, 100), (-1j)), # checked
    ((101, 101), (150, 101), (1)): ((50, 151), (1, 151), (-1)), # correced
    ((51, 101), (100, 101), (1)): ((51, 101), (51, 150), (-1j)), # corrected
    ((1, 50), (50, 50), (-1)): ((150, 0), (101, 0), (1)), # checked
    ((100, 1), (100, 50), (-1j)): ((51, 50), (100, 50), (1)), # checked
}

ext_side_mappings = dict(side_mappings)
for k, v in side_mappings.items():
    s1, e1, d1 = k
    s2, e2, d2 = v
    ext_side_mappings[(s2, e2, -d2)] = (s1, e1, -d1)

def points(start, end):
    pts = []
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    if dx != 0:
        for k in range(0, dx+dx//abs(dx), dx//abs(dx)):
            pts.append((start[0]+k, start[1]))

    if dy != 0:
        for k in range(0, dy+dy//abs(dy), dy//abs(dy)):
            pts.append((start[0], start[1]+k))
    return pts

mappings = {}
for k, v in ext_side_mappings.items():
    s1, e1, d1 = k
    s2, e2, d2 = v
    for pt1, pt2 in zip( points(s1, e1), points(s2, e2)):
        mappings[(pt1, d1)] = (pt2, d2)

#print(mappings)

start= complex(int(start.real), int(start.imag))
#pretty_print(mp, start)

if cur:
    instructions.append(int(cur))

dr = 1

try:
    for inst in instructions:
        #print(inst)
        if type(inst) is int:
            for k in range(inst):
                cur = start+dr
                #print(start, cur)
                #print(mp[int(cur.imag), int(cur.real)])
                if mp[int(cur.imag), int(cur.real)] == 2:
                    start = cur
                    visited[start] = drtoch(dr)
                elif mp[int(cur.imag), int(cur.real)] == 1:
                    break
                else:
                    #print(f'from {cur}')
                    nxt, d = mappings[((int(cur.imag), int(cur.real)), dr)]
                    nxt = nxt[1]+1j*nxt[0]
                    p = nxt+d
                    #print(f'to {nxt}+{d}')
                    #pretty_print(mp, start)
                    if mp[int(p.imag), int(p.real)] == 1:
                        print("Rock!")
                        break
                    start = p
                    dr = d
                    # new_dir = -dr
                    # p = start+new_dir
                    # while mp[int(p.imag), int(p.real)] != 0:
                    #     p = p+new_dir
                    # p = p-new_dir
                    # if mp[int(p.imag), int(p.real)] == 1:
                    #     continue
                    # start = p

                    visited[start] = drtoch(dr)

        else:
            if inst == 'R':
                dr *= 1j
            elif inst == 'L':
                dr *= -1j
        # print()
        # print()
        #pretty_print(mp, start)
        #print(start)
except:
    pretty_print(mp, start)
    print("ERORR")
    print(start)


pretty_print(mp, start)
#print(hor_changes)
#print(ver_changes)

facing = 0
if dr == 1:
    facing = 0
elif dr == -1:
    facing = 2
elif dr == 1j:
    facing = 1
else:
    facing = 3
row = int(start.imag)
col = int(start.real)
print(row, col)
print(1000*(row) + 4*(col)+facing)