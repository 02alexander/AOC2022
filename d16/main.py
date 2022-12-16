#!/usr/bin/env python3

from collections import deque
import sys
from itertools import permutations, chain, combinations
from math import *
from collections import defaultdict
from copy import copy
from tqdm import tqdm
lines = sys.stdin.readlines()



class Node:
    def __init__(self, nexts, label, rate):
        self.nexts = nexts
        self.label = label
        self.rate = rate
    def __str__(self):
        return f'({self.label, self.rate})'
    def __repr__(self):
        return f'({self.label, self.rate})'

# class Namedtuple('Node', ['nexts', 'label', 'rate']):
#     pass

def shortest_path(start, end):
    global graph
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        cur, dist = queue.popleft()
        if cur == end:
            return dist
        if cur not in visited:
            for child in graph[cur].nexts:
                queue.append((child, dist+1))
        visited.add(cur)

def upper_bound(timeleft, cur_rate):
    global maxrate
    return ceil(timeleft/2)*maxrate*timeleft//2 + timeleft*cur_rate

def best_flow(visited, node, timeleft, totflow, cur_best):
    global small_graph, graph
    timeleft = timeleft-1
    totflow += graph[node].rate*timeleft
    if timeleft <= 0:
        #print("Times up!")
        return totflow
    if upper_bound(timeleft, 0)+totflow < cur_best:
        print(f"Upper bound is {upper_bound(timeleft, 0)+totflow}, cur_best={cur_best}")
        return totflow
    
    cur_best = max(cur_best, totflow)
    visited.add(node)
    old_totflow = totflow
    for (next_node, dist) in small_graph[node]:
        #print("hejsan")
        if next_node.label in visited:
            continue
        new_timeleft = timeleft-dist
        if new_timeleft <= 0:
            continue
        totflow = max(totflow, best_flow(copy(visited), next_node.label, new_timeleft, old_totflow, cur_best))
    return totflow

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def best_flow_subset(visited, node, timeleft, totflow, cur_best, subset):
    global small_graph, graph
    timeleft = timeleft-1
    if timeleft <= 0:
        return totflow
    totflow += graph[node].rate*timeleft
    if upper_bound(timeleft, 0)+totflow < cur_best:
        print(f"Upper bound is {upper_bound(timeleft, 0)+totflow}, cur_best={cur_best}")
        return totflow
    
    cur_best = max(cur_best, totflow)
    visited.add(node)
    old_totflow = totflow
    for (next_node, dist) in small_graph[node]:
        if (next_node.label in visited):
            continue
        if (next_node.label not in subset):
            continue
        new_timeleft = timeleft-dist
        if new_timeleft <= 0:
            continue
        totflow = max(totflow, best_flow_subset(copy(visited), next_node.label, new_timeleft, old_totflow, cur_best, subset))
    return totflow


maxrate = 0
nonzeros = set()
graph = {}
for line in lines:
    words = line.split()
    label = words[1]
    rate = int(words[4].split('=')[1][:-1])
    last = ''.join(words[9:]).split(',')
    nexts = eval(f'({last})')
    graph[label] = Node(nexts, label, rate)
    maxrate = max(rate, maxrate)
    if rate != 0:
        nonzeros.add(graph[label])

small_graph = defaultdict(list)
for node1 in nonzeros:
    for node2 in nonzeros:
        if node1.label != node2.label:
            small_graph[node1.label].append((node2, shortest_path(node1.label, node2.label)))



def best_run(subset, delta=0):
    best = 0
    for start_node in subset:
        start_dist = shortest_path("AA", start_node)
        flow = best_flow_subset(set(), start_node, 30-start_dist-delta, 0, 0, subset)
        best = max(best, flow)
    return best

def part1():
    global nonzeros
    nz = set(t.label for t in nonzeros)
    flow = best_run(nz)
    print(flow)

def part2():
    pws = list(powerset(nonzeros))
    best = 0
    for elefant_set in tqdm(pws):
        human_set = nonzeros.difference(elefant_set)

        hum_flow = best_run(human_set, 4)
        elf_flow = best_run(elefant_set, 4)

        if hum_flow+elf_flow > best:
            best = hum_flow+elf_flow
    print(best)

part1()