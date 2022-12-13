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
        #print(a[i], b[i])
        if type(a[i]) == int:
            if type(b[i]) == int:
                #print(f"int int {a[i]} {b[i]}")
                if a[i] > b[i]:
                    return False
                elif a[i] < b[i]:
                     return True
            if type(b[i]) is list:
                #print("int list")
                res = lt([a[i]], b[i])
                #print(f'res={res}')
                if res is not None:
                    return res
        else:
            if type(b[i]) is list:
                #print(f'list list {a[i]} {b[i]}')
                res = lt(a[i], b[i])
                #print(f'res={res}')
                if res is not None:
                    return res      
            if type(b[i]) == int:
                #print(f"list int {a[i]} {b[i]}")
                res = lt(a[i], [b[i]])
                #print(res)
                if res is not None:
                    return res

    if len(a) > len(b):
        return False
    elif len(b) > len(a):
        return True
    
    return None
            

lines  = [ eval(g) for group in groups for g in group.split('\n') ]
#print(lines)
lines.append([[2]])
lines.append([[6]])
lines = sorted(lines, key=cmp_to_key(lambda a,b : {True: -1, False: 1, None: 0}[lt(a,b)]))
#lines.sort(key=lambda l: len(l))
for line in lines:
    print(line)
print(lines.index([[2]])+1)
print(lines.index([[6]])+1)
print((lines.index([[2]])+1)*(lines.index([[6]])+1))


        
# cnt = 0
# for i, group in enumerate(groups):
#     left, right = group.split('\n')
#     #left = left.replace('[', '(')
#     #left = left.replace(']', ')')
#     #print(left)
#     left = eval(left)
#     #right = right.replace('[', '(')
#     #right = right.replace(']', ')')
#     #print(right)
#     right = eval(right)

#     #res = lt(left, right)
#     if left < right:
#         cnt += 1+i
# print(cnt)
