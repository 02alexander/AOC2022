#!/usr/bin/env python3 
import sys

groups = sys.stdin.read().split('\n\n')
#inp = sys.stdin.read()

monkeys = []

PART = 1

class Monkey:
    def __init__(self, label, starting_items, op, test, throw1, throw2):
        self.label = label
        self.nbinspections = 0
        self.items = starting_items
        self.op = op
        self.test = test
        self.throw1 = throw1
        self.throw2 = throw2
        self.mod = None
    
    def round(self):
        global monkeys
        for item in self.items:

            self.nbinspections += 1
            #print("inspecting: ", self.label, item)
            item = self.op(item)
            #print(item)

            if self.mod:
                item = item % self.mod
            else:
                item = item //3

            if item % self.test == 0:
                monkeys[self.throw1].items.append(item)
            else:
                monkeys[self.throw2].items.append(item)
        self.items = []

def part1():
    global monkeys
    monkeys = []
    md = 1
    for i, group in enumerate(groups):
        lines = group.split('\n')
        starting_items = list(map(int, lines[1].split(':')[1].split(',')))
        op = lines[2].split('=')[1]
        op = eval(f'lambda old: {op}')
        test = int(lines[3].split()[-1])
        md *= test
        t1 = int(lines[4].split()[-1])
        t2 = int(lines[5].split()[-1])
        monkeys.append(Monkey(i, starting_items, op, test, t1, t2))

    
    PART = 1
    for _ in range(20):
        for monkey in monkeys:
            monkey.round()

    nbi = []
    for monkey in monkeys:
        nbi.append(monkey.nbinspections)
    nbi.sort()
    print(nbi[-1]*nbi[-2])

def part2():
    global monkeys
    md = 1
    monkeys = []
    for i, group in enumerate(groups):
        lines = group.split('\n')
        starting_items = list(map(int, lines[1].split(':')[1].split(',')))
        op = lines[2].split('=')[1]
        op = eval(f'lambda old: {op}')
        test = int(lines[3].split()[-1])
        md *= test
        t1 = int(lines[4].split()[-1])
        t2 = int(lines[5].split()[-1])
        monkeys.append(Monkey(i, starting_items, op, test, t1, t2))
    for _ in range(10000):
        for monkey in monkeys:
            monkey.mod = md
            monkey.round()
    nbi = []
    for monkey in monkeys:
        nbi.append(monkey.nbinspections)
    nbi.sort()
    print(nbi[-1]*nbi[-2])

part1()
part2()