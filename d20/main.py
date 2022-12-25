#!/usr/bin/env python3

from math import *
import sys
from copy import copy
from collections import defaultdict
lines = sys.stdin.readlines()

lst = []
for ident, line in enumerate(lines):
    lst.append((int(line), ident))

ln = len(lst)
orig = list(lst)
for elem, ident in orig:
    for i in range(len(lst)):
        if lst[i] == (elem, ident):
            k = elem
            if k == 0:
                sign = 1
            else:
                sign = k//abs(k)
            
            #print(f'\nmix {k}')
            for di in range(0, k, sign):
                lst[(i+di) % ln], lst[(i+sign+di) % ln] = lst[(i+sign+di) % ln], lst[(i+di) % ln]
            #print([v for v , _b in lst])
            break

print(lst)

zeroidx = list(map(lambda t: t[0], lst)).index(0)
a = lst[ (zeroidx+1000)%ln ][0]
b = lst[ (zeroidx+2000)%ln ][0]
c = lst[ (zeroidx+3000)%ln ][0]
print(a, b, c)
print(a+b+c)

# 12767
# -11365
# 18257