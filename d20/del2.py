#!/usr/bin/env python3
import sys
from tqdm import tqdm

def mix(lst, order):
    ln = len(lst)
    for elem, ident in tqdm(order):
        i = lst.index((elem, ident))
        k = elem % (ln-1)
        for di in range(0, k):
            idx1 = (i+di) % ln
            idx2 = (i+1+di) % ln
            lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    return lst

lines = sys.stdin.readlines()
#key=811589153
#key = 1

lst = []

for ident, line in enumerate(lines):
    lst.append((key*int(line), ident))
ln = len(lst)

orig = list(lst)
for _ in range(1):
    mix(lst, orig)
    zeroidx = list(map(lambda t: t[0], lst)).index(0)
    print([ lst[(zeroidx+i)%ln][0] for i in range(ln) ])

zeroidx = list(map(lambda t: t[0], lst)).index(0)
a = lst[ (zeroidx+1000)%ln ][0]
b = lst[ (zeroidx+2000)%ln ][0]
c = lst[ (zeroidx+3000)%ln ][0]
print(a+b+c)

# 12767
# -11365
# 18257