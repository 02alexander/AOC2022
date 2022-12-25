#!/usr/bin/env python3

from functools import cache
from collections import namedtuple
import sys
import re
from copy import deepcopy, copy


def init_nt(nt, blueprint):
    nt.robots = (1, 0, 0, 0)
    nt.blueprint = blueprint
    nt.minerals = (0, 0, 0, 0)
    nt.time = 24
    #nt.hist = []

def step(nt):
    nt.minerals = tuple(map(lambda t: t[0]+t[1], zip(nt.robots, nt.minerals)  ))
    nt.time -= 1

def buy_drill(nt, drill_type):
    #nt.robots[drill_type] += 1
    #nt.hist.append((25-nt.time, drill_type))
    nt.robots = tuple( (nt.robots[i] + (1 if drill_type==i else 0)) for i in range(4) )
    nt.minerals = tuple(map(lambda t: t[0]-t[1], zip(nt.minerals, nt.blueprint[drill_type])  ))

def can_buy(nt, drill_type):
    #print(nt.minerals, nt.blueprint[drill_type], [i for i in range(4)])
    return all(map(lambda i: nt.minerals[i] >= nt.blueprint[drill_type][i], (i for i in range(4))))

def repr_nt(nt):
    return f'{nt.robots} {nt.minerals}, {nt.time} \n {nt.blueprint} \n {nt.hist}'

def cpy(nt):
    new = namedtuple('Mine', ('robots', 'blueprint', 'minerals', 'time'))
    new.robots = copy(nt.robots)
    new.blueprint = copy(nt.blueprint)
    new.minerals = copy(nt.minerals)
    new.time = copy(nt.time)
    return new

def min_time_needed(nt, nb_geodes):
    needed = nb_geodes-nt.minerals[3]
    if nt.robots[3] == 0:
        if nt.robots[2] == 0:
            return needed//2+ (nt.blueprint[3][2]) // 2
        else:
            return needed//2
    return 0

lines = sys.stdin.readlines()

blueprints = []
for line in lines:
    ints = list(map(int, re.findall('([0-9.]*[0-9]+)', line)))
    #print(ints)
    odc = ( ints[1], 0, 0, 0 )
    cdc = (ints[2], 0, 0, 0)
    obdc = (ints[3], ints[4], 0, 0)
    gdc = (ints[5] , 0, ints[6], 0)
    blueprint = (odc, cdc, obdc, gdc)
    blueprints.append(blueprint)


cnt = 0

@cache
def dfs(mine):
    global cnt
    
    best_geodes = -1

    if mine.time < 1:
        # if mine.minerals[-1] == 11:
        #         print("SUPER")
        #         print(repr_nt(mine))
        #         print("SUPER")
        return mine.minerals[-1]
    
    #print(mine.blueprint)
    #print(needed)
    needed = [ max(t[i] for t in mine.blueprint) for i in range(3) ] + [10000]

    #needed[1] //= 2
    #needed[2] //= 2

    #needed = [1, 4, 2, 2]
    #print([n//2 for n in needed])

    for i in range(4):
        if mine.robots[i] >= needed[i]:
            #print(i, "unnecessary")
            continue
        cnt += 1

        new_mine = cpy(mine)


        imp = False
        while not can_buy(new_mine, i):
            if new_mine.time <= 1:
                imp = True
                break
            step(new_mine)
        if imp:
            #print()
            #print(repr_nt(new_mine))
            #print(f"imp {i}")
            # if new_mine.minerals[-1] == 11:
            #     print("SUPER")
            #     print(repr_nt(new_mine))
            #     print("SUPER")
            best_geodes = max(best_geodes, new_mine.minerals[-1])
            continue

        step(new_mine)

        #if i == 3 and new_mine.robots[i] == 0 and new_mine.time == 6:
        #    print(repr_nt(new_mine))
        buy_drill(new_mine, i)
        for mat in new_mine.minerals:
            if mat < 0:
                print("ERROR")
        #for mat in new_mine.materials:

        # if i == 3 and new_mine.robots[i] == 1 and new_mine.time == 8:
        #    print()
        #    print(repr_nt(new_mine))

        #if new_mine.minerals[-1] > best_geodes:
        #    print(repr_nt(new_mine))
        
        best_geodes = max(best_geodes, dfs(cpy(new_mine)))
    
    while mine.time >= 1:
        step(mine)

    # if mine.minerals[-1] == 11:
    #     print("SUPER")
    #     print(repr_nt(mine))
    #     print("SUPER")

    return max(best_geodes, mine.minerals[-1])

#mine = namedtuple('Mine', ('robots', 'blueprint', 'minerals', 'time', 'hist'))
#init_nt(mine, blueprint[0])
#mp = { mine: 0 }
#print(mp[mine])

sm = 0
for i, blueprint in enumerate(blueprints[:]):

    mine = namedtuple('Mine', ('robots', 'blueprint', 'minerals', 'time'))
    init_nt(mine, blueprint)
    mine.time = 32

    # print(repr_nt(mine))
    res = dfs(cpy(mine))
    print(cnt)
    cnt = 0
    dfs.cache_clear()
    print(res*(i+1))
    sm += (res*(i+1))

print(sm)


# print(repr_nt(mine))
# new_mine = mine

# hist = [(3, 1), (5, 1), (7, 1), (10, 2), (15, 2), (16, 3), (20, 3)]

# for i in range(1, 24+1):

#     step(mine)    
#     print(f'step {i}')
#     print(repr_nt(mine))
#     for (t, d) in hist:
#         if i == t:
#             print(f"buys {d}")
#             buy_drill(mine, d)
#     print()

    
#     # if i == 3:
#     #     buy_drill(mine, 1)
#     # if i == 5:
#     #     buy_drill(mine, 1)
#     # if i == 7:
#     #     buy_drill(mine, 1)
#     # if i == 11:
#     #     buy_drill(mine, 2)
#     # if i == 12:
#     #     buy_drill(mine, 1)
    
#     # if i == 15:
#     #     buy_drill(mine, 2)

#     # if i == 18:
#     #     buy_drill(mine, 3)

#     # if i == 21:
#     #     buy_drill(mine, 3)


# print()
# print(repr_nt(mine))
