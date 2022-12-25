#!/usr/bin/env python3

import sys
from collections import defaultdict
lines = sys.stdin.readlines()

ground = set()
elves_pos = dict()
for row, line in enumerate(lines):
    for col, ch in enumerate(line.strip()):
        if ch == '#':
            elves_pos[col-row*1j] = [0, 1, 2, 3]


def mx_real(pos):
    return max(pos, key=lambda t: int(t.real))
def mn_real(pos):
    return min(pos, key=lambda t: int(t.real))
def mx_imag(pos):
    return max(pos, key=lambda t: int(t.imag))
def mn_imag(pos):
    return min(pos, key=lambda t: int(t.imag))

def pretty_print(pos):
    pos = set(pos.keys())
    mxr = int(mx_real(pos).real)
    mnr = int(mn_real(pos).real)
    mxi = int(mx_imag(pos).imag)
    mni = int(mn_imag(pos).imag)
    print(mnr, mxr, mni, mxi)
    ground = (mxi-mni+1)*(mxr-mnr+1)
    for im in range(mxi, mni-1, -1):
        for rl in range(mnr, mxr+1): 
            if (rl+1j*im) in pos:
                print('#', end="")
                ground -= 1
            else:
                print(".", end="")
        print()
    print(ground)

print(elves_pos)
#print(min(elves_pos, key=lambda z: float(z.imag)))
#print([ int(z.imag) for z in elves_pos])
# print(mn_imag(elves_pos), mx_imag(elves_pos))
pretty_print(elves_pos)
orig_len = len(elves_pos)
for i in range(1,100000000000):
    cnt = defaultdict(list)
    updates = []
    no_moves = True
    for pos, dirs in elves_pos.items():
        c = 0
        for dr in [1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j]:
            if pos+dr in elves_pos:
                c += 1

        l = elves_pos[pos]
        l = l[1:]+l[:1]
        updates.append((pos, l))
        
        if c == 0:
            continue
        
        chosen = None
        for dr in dirs:
            if dr == 0 and pos+1j not in elves_pos and pos+1+1j not in elves_pos and pos-1+1j not in elves_pos:
                cnt[pos+1j].append((pos, dr))
                chosen = dr
                break
        
            if dr == 1 and pos-1j not in elves_pos and pos+1-1j not in elves_pos and pos-1-1j not in elves_pos:
                cnt[pos-1j].append((pos, dr))
                chosen = dr
                break
            
            if dr == 2 and pos-1 not in elves_pos and pos-1+1j not in elves_pos and pos-1-1j not in elves_pos:
                cnt[pos-1].append((pos, dr))
                chosen = dr
                break
            
            if dr == 3 and pos+1 not in elves_pos and pos+1+1j not in elves_pos and pos+1-1j not in elves_pos:
                cnt[pos+1].append((pos, dr))
                chosen = dr
                break
        if chosen:
            no_moves = False
        
    if no_moves:
        break
    
    for pos, l in updates:
        elves_pos[pos] = l
        
    for dst, sources in cnt.items():

        if len(sources) == 1:
            src, dr = sources[0]
            dirs = elves_pos[src]
            del elves_pos[src]

            elves_pos[dst] = dirs
    #print()      
    #pretty_print(elves_pos)
    assert(orig_len == len(elves_pos))
    print(i+1)
