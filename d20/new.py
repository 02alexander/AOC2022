#!/usr/bin/env python3

from math import *
import sys
from copy import copy
from collections import defaultdict
lines = sys.stdin.readlines()

lst = []
for line in lines:
    lst.append((int(line), False))

ln = len(lst)
orig = list(lst)
for elem, _ in orig:
    for i in range(len(lst)):
        if lst[i][0] == elem and not lst[i][1]:
            lst[i] = (lst[i][0], True)
            k = elem
            if k == 0:
                sign = 1
            else:
                sign = k//abs(k)
            
            for di in range(0, k, sign):
                lst[(i+di) % ln], lst[(i+sign+di) % ln] = lst[(i+sign+di) % ln], lst[(i+di) % ln]
            break

print(lst)
zeroidx = lst.index((0, False))
a = lst[ (zeroidx+1000)%ln ][0]
b = lst[ (zeroidx+2000)%ln ][0]
c = lst[ (zeroidx+3000)%ln ][0]
print(a, b, c)
print(a+b+c)

# 12767
# -11365