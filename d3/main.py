#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
#groups = [g.split('\n') for g in sys.stdin.read().strip().split('\n\n')]

c = 0
for i, group in enumerate(lines[::3]):
    group = lines[i*3:i*3+3]
    print(group)
    tot = (set(list(group[0].strip())))    
    for line in group[1:]:
        print(set(list(line.strip())))
        tot = tot.intersection(set(list(line.strip())))

    snitt = tot
    for ch in snitt:
        if ch.islower():
            c += ord(ch)-ord('a')+1
            print(c)
        else:
            c += 27+ord(ch)-ord('A')
    print(snitt)

print(c)