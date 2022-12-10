#!/usr/bin/env python3

import sys

data = sys.stdin.readlines()
count = 0
for line in data:
    a,b = line.strip().split()
    a,b = ord(a)-ord('A'), ord(b)-ord('X')
    # if b == 0:
    #     b = (a-1)%3
    # elif b == 1:
    #     b = a
    # else:
    #     b = (a+1)%3
    
    count += 3*((b-a+1)%3)+b+1
    # if (b-a)%3 == 0:
    #     count += b+1+3
    # elif (b-a)%3 == 1:
    #     count += b+1+6
    # else:
    #     count += b+1

print(count)