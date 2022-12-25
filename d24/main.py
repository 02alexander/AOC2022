#!/usr/bin/env python3

import sys
from collections import deque
from heapq import heapify, heappop, heappush
lines = sys.stdin.readlines()

#mat = [[None for _ in range(len(lines[0])-2)] for _ in range(lines)]

height = len(lines)-2
width = len(lines[0].strip())-2
print(f'height={height}')
print(f'width={width}')
ver_blizzards = [[] for _ in range(width)]
hor_blizzards = [[] for _ in range(height)]

for row, line in enumerate(lines[1:-1]):
    for col, ch in enumerate(line.strip()[1:-1]):
        if ch == '<':
            hor_blizzards[row].append((col, -1))
        elif ch == '>':
            hor_blizzards[row].append((col, 1))
        elif ch == '^':
            ver_blizzards[col].append((row, -1))
        elif ch == 'v':
            ver_blizzards[col].append((row, 1))


def possible_moves(pos, t, start=(-1,0)):
    global hor_blizzards, ver_blizzards
    next_pos = []
    for drow, dcol in [(1, 0), (0, 1), (-1, 0), (0,-1), (0,0)]:
        if pos == start and (drow,dcol) == (0,0):
            next_pos.append(pos)
        newp = (pos[0]+drow, pos[1]+dcol)
        if newp[0] < 0 or newp[1] < 0 or newp[1] >= width or newp[0] >= height:
            continue
        imp = False
        for startp, dr in ver_blizzards[newp[1]]:
            if (startp+t*dr) % height == newp[0]:
                imp = True
                break
        if imp:
            continue
        for startp, dr in hor_blizzards[newp[0]]:
            if (startp+t*dr) % width == newp[1]:
                imp = True
                break
        if imp:
            continue
        next_pos.append(newp)
    return next_pos

def hamil(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def search(start, target, start_t=0):
    visited = set()
    q = [(hamil(start, target)+start_t, start_t, start)]
    heapify(q)
    while len(q) !=0 :
        heur, t, current = heappop(q)
        if (t % width*height, current) in visited:
            continue
        visited.add((t % width*height, current))
        if current == target:
            return t
        for mv in possible_moves(current, t+1, start=start):
            heappush(q, ((hamil(mv, target)+t+1, t+1, mv)))


start = (-1, 0)
nstart = (0,0)
target = (height, width-1)
ntarget = (height-1, width-1)
#target = (0, 1)
print(f'start={start}')
print(f'target={target}')


t1 = search(start, ntarget)+1
print(t1)
t2 = search(target, nstart, start_t=t1)+1
print(t2)
t3 = search(start, ntarget, start_t=t2)+1
print(t1, t2, t3)

print(possible_moves(target, 3, start=target))

