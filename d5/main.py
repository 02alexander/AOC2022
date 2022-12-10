#!/usr/bin/env python3
import sys
data = sys.stdin.read()

fh, lh = data.split('\n\n')

print(fh)

lines = fh.splitlines()
count = (len(lines[-1])+1)//4
print(count)

stacks = [
    [] for _ in range(count)
]
print()
for line in lines[:-1]:
    for c in range(count):
        ch = line[c*4+1]
        #print(c*4+1)
        if ch != ' ':
            stacks[c].append(ch)
print(stacks)

stacks = [ list(reversed(stack)) for stack in stacks ]

for line in lh.splitlines():
    tokens = line.split()
    n = int(tokens[1])
    src = int(tokens[3])-1
    dst = int(tokens[5])-1
    
    # del 1
    #stacks[dst] += (reversed(stacks[src][-n:]))
    
    # del 2
    stacks[dst] += (stacks[src][-n:])
    
    del stacks[src][-n:]
    #print(stacks)

print(stacks)
print(''.join( stacks[c][-1] for c in range(count) ))