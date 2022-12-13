#!/usr/bin/env python3 
import sys

lines = sys.stdin.readlines()
intcycles = [20, 60, 100, 140, 180, 220]
vals = []
img = ""

x = 1
cycle = 1
cur_ins = None
for line in lines:

    toks = line.strip().split()
    if toks[0] == "noop":
        cur_ins = ("noop", 0, None)
    elif toks[0] == "addx":
        cur_ins = ("add", 1, int(toks[1]))

    while cur_ins is not None:
        if (cycle-1)%40  == 0:
            img += "\n"
        if abs(x-(cycle-1)%40) <= 1:
            img += "#"
        else:
            img += "."
        if cycle in intcycles:
            vals.append(x)
        if cur_ins:
            ins, tm, y = cur_ins
            if tm == 0:
                if ins == "add":
                    x += y
                cur_ins = None
            else:
                cur_ins = (ins, tm-1, y)
            
        cycle += 1

sm = 0
for c, v in zip(intcycles, vals):
    sm += c*v
print(sm)

print(img)