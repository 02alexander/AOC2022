#!/usr/bin/env python3 
import sys
import numpy as np

lines = sys.stdin.readlines()

def are_adj(k1, k2):
    return abs(k1[0]-k2[0]) < 2 and abs(k1[1]-k2[1]) < 2

def move_towards(head, tail):
    return (
        tail[0] + max(-1, min(1, (head[0]-tail[0]))),
        tail[1] + max(-1, min(1, (head[1]-tail[1])))
    )

def sim_rope(nbknots):

    visited = set()
    knots = [np.array((0,0)) for _ in range(nbknots)]
    visited.add((0,0))

    for line in lines:
        D, c = line.strip().split()
        c = int(c)
        if D == "L":
            dr = (-1, 0)
        elif D == "U":
            dr = (0,1)
        elif D == "R":
            dr = (1,0)
        elif D == "D":
            dr = (0,-1)
        else:
            print("ERROR")
        dr = np.array(dr)
        for i in range(c):
            knots[-1] += dr
            for i in reversed(range(0, len(knots)-1)):
                if not are_adj(knots[i+1], knots[i]):
                    knots[i] = move_towards(knots[i+1], knots[i])
            visited.add(tuple(knots[0]))
            
    return len(visited)

print(sim_rope(2))
print(sim_rope(10))