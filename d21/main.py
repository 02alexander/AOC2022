#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def check(human_val, monkeys, nonints):

    ln = len(monkeys.items())
    monkeys['humn'] = human_val
    while len(nonints) != 0:
        rm = None
        for monkey in nonints:
            n1, op, n2 = monkeys[monkey]
            if n1 not in nonints and n2 not in nonints:
                if monkey == 'root':
                    return monkeys[n1] - monkeys[n2]
                else:
                    monkeys[monkey] = eval(f'{monkeys[n1]} {op} {monkeys[n2]}')
                    rm = (monkey)
                    break
        if rm:
            nonints.remove(monkey)


nonints = set()
monkeys = {}
for line in lines:
    toks = line.strip().split()
    name = toks[0][:-1]
    if len(toks) > 2:
        nonints.add(name)
        if toks[2] == '/':
            op = '//'
        else:
            op = toks[2] 
        monkeys[name] = [toks[1], op, toks[3]]
    else:
        monkeys[name] = (int(toks[1]))

#print(check(301, dict(monkeys), set(nonints)))


MIN = 0
MAX = 100000000000000000

while True:
    val = (MAX+MIN)//2
    print()
    print(f'iteration {val}')
    diff = check(val, dict(monkeys), set(nonints))
    print(diff)
    if diff == 0:
        break

    if diff > 0:
        MIN = val
    else:
        MAX = val


print(monkeys['root'])