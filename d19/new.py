#!/usr/bin/env python3 
import sys

import itertools
import re

lines = sys.stdin.readlines()
#inp = sys.stdin.read()

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


blueprints = []
for line in lines:
    ints = list(map(int, re.findall('([0-9.]*[0-9]+)', line)))
    odc = ( ints[1], 0, 0, 0 )
    cdc = (ints[2], 0, 0, 0)
    obdc = (ints[3], ints[4], 0, 0)
    gdc = (ints[5] , 0, ints[6], 0)
    blueprint = (odc, cdc, obdc, gdc)
    blueprints.append(blueprint)


blueprints = []
for line in lines:
    ints = list(map(int, re.findall('([0-9.]*[0-9]+)', line)))
    odc = ( ints[1], 0, 0, 0 )
    cdc = (ints[2], 0, 0, 0)
    obdc = (ints[3], ints[4], 0, 0)
    gdc = (ints[5] , 0, ints[6], 0)
    blueprint = (odc, cdc, obdc, gdc)
    blueprints.append(blueprint)


nturns = 24
mxm = nturns*(nturns+1)//2
cnt = 0
for blueprint in blueprints[:]:
    max_robots = [ max(t[i] for t in blueprint) for i in range(3) ] + [5]
    for a, b, c, d in itertools.product( *[range(1, max_robots[i]) for i in range(4) ]):
        bought_robots = (a, b, c, d)
        
        needed_res = [0,0,0,0]
        for nrobots, cost in zip(bought_robots, blueprint):
            for i in range(4):
                needed_res[i] += nrobots*cost[i]
        #print(bought_robots)
        #print(mxm)
        #print(needed_res)
        if sum(needed_res) > mxm:
            continue
        
        if a+b+c+d > nturns:
            continue
        cnt += 1
        #print(list(zip(bought_robots, blueprint)))
        #print(a,b,c,d)
        #print(needed_res)

    print(cnt)
    cnt = 0
