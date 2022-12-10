#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

count = 0
sts = []
for line in lines:
    r1, r2 = line.strip().split(',')
    r1 = list(range(int(r1.split('-')[0]), int(r1.split('-')[1])+1))
    r2 = list(range(int(r2.split('-')[0]), int(r2.split('-')[1])+1))
    # if set(r1).issubset(set(r2)) or set(r2).issubset(set(r1)) :
    #     count += 1    
    if len(set(r1).intersection(set(r2))) != 0:
        count += 1


print(count)