#!/usr/bin/env python3

from functools import cache
from collections import namedtuple
import sys
import re
from copy import deepcopy, copy
lines = sys.stdin.readlines()


class Drill:
    def __init__(self, label, ore_drill_cost, clay_drill_cost, obdc, geode_drill_cost):
        self.label = label
        self.odc = ore_drill_cost
        self.fdc = clay_drill_cost
        self.obdc = obdc
        self.gdc = geode_drill_cost

    def __repr__(self):
        return f'[{self.label} {self.odc}, {self.fdc}, {self.obdc}, {self.gdc} ]'


# class Mine:
#     def __init__(self, blueprint):
#         self.robots = [1, 0, 0, 0]
#         self.blueprint = blueprint
#         self.minerals = [0, 0, 0, 0]
#         self.time = 1

#     def step(self):
#         self.minerals = list(map(lambda t: t[0]+t[1], zip(self.robots, self.minerals)  ))
#         self.time += 1

#     def buy_drill(self, drill_type):
#         self.robots[drill_type] += 1
#         self.minerals = list(map(lambda t: t[0]-t[1], zip(self.minerals, self.blueprint[drill_type])  ))

#     def can_buy(self, drill_type):
#         #print(self.minerals, self.blueprint[drill_type], [i for i in range(4)])
#         return all(map(lambda i: self.minerals[i] >= self.blueprint[drill_type][i], (i for i in range(4))))

#     def __repr__(self):
#         return f'{self.robots} {self.minerals}, {self.time} \n {self.blueprint}'

def init_nt(nt, blueprint):
    nt.robots = (1, 0, 0, 0)
    nt.blueprint = blueprint
    nt.minerals = (0, 0, 0, 0)
    nt.time = 24

def step(nt):
    nt.minerals = tuple(map(lambda t: t[0]+t[1], zip(nt.robots, nt.minerals)  ))
    nt.time -= 1

def buy_drill(nt, drill_type):
    #nt.robots[drill_type] += 1
    nt.robots = tuple( (nt.robots[i] + (1 if drill_type==i else 0)) for i in range(4) )
    nt.minerals = tuple(map(lambda t: t[0]-t[1], zip(nt.minerals, nt.blueprint[drill_type])  ))

def can_buy(nt, drill_type):
    #print(nt.minerals, nt.blueprint[drill_type], [i for i in range(4)])
    return all(map(lambda i: nt.minerals[i] >= nt.blueprint[drill_type][i], (i for i in range(4))))

def repr_nt(nt):
    return f'{nt.robots} {nt.minerals}, {nt.time} \n {nt.blueprint}'

def cpy(nt):
    new = namedtuple('Mine', ['robots', 'blueprint', 'minerals', 'time'])
    new.robots = copy(nt.robots)
    new.blueprint = copy(nt.blueprint)
    new.minerals = nt.minerals
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
    #drill = Drill(ints[0], odc, cdc, obdc, gdc)

    #print(drill)

#mine = Mine(blueprints[0])
#print(repr_nt(mine))

#lim = 20000000000
#cnt = 0
for i, blueprint in enumerate(blueprints):
    def dfs(mine, best_geodes=None):
        global lim, cnt
        #if cnt >= lim:
        #    return 0
        #cnt += 1
        
        if not best_geodes:
            best_geodes = -1

        if min_time_needed(mine, best_geodes+1) >= mine.time:
            return 0
        if mine.time < 1:
            return mine.minerals[-1]
        needed = [ max(t[i] for t in mine.blueprint) for i in range(3) ] + [10000]

        #print(needed)
        
        for i in reversed(range(4)):
            if can_buy(mine, i) and mine.robots[i] < needed[i]:

                new_mine = cpy(mine)
                step(new_mine)
                buy_drill(new_mine, i)

                best_geodes = max(best_geodes, dfs(cpy(new_mine), best_geodes))
                if i == 3 or i == 2:
                    break
        step(mine)
        best_geodes = max(best_geodes, dfs(cpy(mine), best_geodes))

        return max(best_geodes, mine.minerals[-1])


    mine = namedtuple('Mine', ('robots', 'blueprint', 'minerals', 'time'))
    mp = {  mine: 0}
    #print(mp[mine])
    init_nt(mine, blueprint)
    #print(type(mine))
    #print(tuple(mine))
    #print(f'blueprint={mine.blueprint}')

    mine.time = 24

    # print(repr_nt(mine))
    res = dfs(cpy(mine))
    #dfs.cache_clear()
    print(res*(i+1))
#print("done")

# print(repr_nt(mine))


# for _ in range(1, 24):

    
#     print(repr_nt(mine))
#     step(mine)

#     for i in reversed(range(4)):
#         if i != 3:
#             if can_buy(mine, i) and mine.minerals[i] < mine.blueprint[i+1][i]:
#                 print(f'buys {i}')
#                 buy_drill(mine, i)
#                 break
#         elif can_buy(mine, i):
#             print(f'buys {i}')
#             buy_drill(mine, i)
#             break

#     print()
#     print(mine.time)
#     print()

# print(repr_nt(mine))
