#!/usr/bin/env python3 
import sys

lines = sys.stdin.readlines()

for line in lines:
    line = line.strip()
    for i in range(len(line)-14):
        s = set(list(line[i:i+14]))
        if len(s) == 14:
            print(i+14)
            break


