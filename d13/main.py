#!/usr/bin/env python3 
import sys
from functools import cmp_to_key

#lines = sys.stdin.readlines()
#inp = sys.stdin.read()
groups = sys.stdin.read().split('\n\n')

def lt(a, b):
    if len(a) == 0 and len(b) == 0:
            return None
    elif len(a) == 0:
        return True
    elif len(b) == 0:
        return False
    i = 0
    for i in range(min(len(a), len(b))):
        if type(a[i]) == int:
            if type(b[i]) == int:
                if a[i] > b[i]:
                    return False
                elif a[i] < b[i]: 
                    return True
            if type(b[i]) is list:
                res = lt([a[i]], b[i])
                if res is not None: 
                    return res
        else:
            if type(b[i]) is list:
                res = lt(a[i], b[i])
                if res is not None: 
                    return res      
            if type(b[i]) == int:
                res = lt(a[i], [b[i]])
                if res is not None: 
                    return res

    if len(a) > len(b):
        return False
    elif len(b) > len(a):
        return True
    
    return None
            
def part2():
    lines  = [ eval(g) for group in groups for g in group.split('\n') ]
    lines.append([[2]])
    lines.append([[6]])
    lines = sorted(lines, key=cmp_to_key(lambda a,b : {True: -1, False: 1, None: 0}[lt(a,b)]))
    print((lines.index([[2]])+1)*(lines.index([[6]])+1))


def part1():
    cnt = 0
    for i, group in enumerate(groups):
        left, right = group.split('\n')
        left = eval(left)
        right = eval(right)

        cm = lt(left, right)
        if cm:
            cnt += 1+i
    print(cnt)

part1()    
part2()