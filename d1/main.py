#!/usr/bin/env python3

import sys
"""
lines = sys.stdin.readlines()
elves = []
cur_elf = 0
for line in lines:
    line = line.strip()
    if not line:
        elves.append(cur_elf)
        cur_elf = 0
    else:
        cur_elf += int(line)
elves.sort(reverse=True)
print(sum(elves[:3]))
"""

print(sum(sorted( sum(map(int,  g.split('\n'))) for g in sys.stdin.read().split('\n\n') )[-3:]))