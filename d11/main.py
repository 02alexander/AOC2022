#!/usr/bin/env python3 
import sys

groups = sys.stdin.read().split('\n\n')
#inp = sys.stdin.read()

monkeys = []

md = 1

class Monkey:
    def __init__(self, label, starting_items, op, test, throw1, throw2):
        self.label = label
        self.nbinspections = 0
        self.items = starting_items
        self.op = op
        self.test = test
        self.throw1 = throw1
        self.throw2 = throw2
    
    def round(self):
        global monkeys
        for item in self.items:

            self.nbinspections += 1
            #print("inspecting: ", self.label, item)
            item = self.op(item)
            #print(item)

            #item = item //3
            item = item % md

            if item % self.test == 0:
                monkeys[self.throw1].items.append(item)
                #print(f"threw to monkey {self.throw1}")
            else:
                #print(f"threw to monkey {self.throw2}")
                monkeys[self.throw2].items.append(item)
        self.items = []

    
#print(groups)
for i, group in enumerate(groups):
    lines = group.split('\n')
    #print(lines)
    starting_items = list(map(int, lines[1].split(':')[1].split(',')))
    op = lines[2].split('=')[1]
    op = eval(f'lambda old: {op}')
    test = int(lines[3].split()[-1])
    md *= test
    t1 = int(lines[4].split()[-1])
    t2 = int(lines[5].split()[-1])
    print(i, starting_items, test, t1, t2)
    monkeys.append(Monkey(i, starting_items, op, test, t1, t2))


for _ in range(10000):
    for monkey in monkeys:
        monkey.round()

nbi = []
for monkey in monkeys:
    #print(monkey.items)
    nbi.append(monkey.nbinspections)
    print(monkey.nbinspections)

nbi.sort()
print(nbi[-1]*nbi[-2])