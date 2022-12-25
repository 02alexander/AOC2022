#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
import itertools

points = set()
for line in lines:
    words = line.strip().split(',')
    points.add(tuple(map(int, words)))

directions = [ (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1) ]

maxx = [max(p[i] for p in points) for i in range(3)]
minx = [min(p[i] for p in points) for i in range(3)]

tot = 0
for point in points:
    cnt = 6
    for dr in directions:
        res = tuple(map(lambda t: t[0]+t[1],zip(point, dr)))
        if res in points: cnt -= 1
    tot += cnt
def inner_size(start_point):
    if start_point in points:
        return (0, {start_point})
    visited = set()
    nxt = [start_point]
    cnt = 0
    while nxt:
        cur = nxt.pop()
        if cur in visited:
            continue
        visited.add(cur)
        for dr in directions:
            res = tuple(map(lambda t: t[0]+t[1],zip(cur, dr)))
            for i in range(3):
                if res[i] < minx[i] or res[i] > maxx[i]:
                    return (0, {start_point})
            if res in points:
                cnt += 1
            elif res not in visited:
                nxt.append(res)
    return (cnt, visited)
print(tot)
visited = set()
for x, y, z in itertools.product(*[range(minx[i], maxx[i]+1) for i in range(3)]):
    point = (x, y, z)
    if point not in visited:
        rem,vis = inner_size(point)
        
        tot -= rem 
        for elem in vis:
            visited.add(elem)


print(tot)





    