#!/usr/bin/env python3
import sys
import numpy as np
from numpy import array as ara

class Shape:
    def __init__(self, pattern, position=None):
        height, width = np.shape(pattern)
        self.width = width
        self.height = height
        self.pos = position
        self.pattern = pattern


class World:
    def __init__(self, width, height, shapes):
        self.blocks = np.zeros((height, width))
        self.shapes = shapes
        self.curshape = 0
        self.mshp = None
        self.maxy = 0
        self.cnt = 0

    def hit_bottom(self, shape):
         return np.sum(np.multiply( self.blocks[
                shape.pos[1]-1:shape.pos[1]-1+shape.height, 
                shape.pos[0]:shape.pos[0]+shape.width, 
            ], shape.pattern ))

    def pretty_print(self):
        rows, cols = np.shape(self.blocks)
        for r in reversed(range(self.maxy+5)):
            for c in range(cols):
                was_true = False
                if self.mshp:
                    if (self.mshp.pos[1] <= r < self.mshp.height+self.mshp.pos[1]) and \
                        (self.mshp.pos[0] <= c < self.mshp.width+self.mshp.pos[0]):
                        if self.mshp.pattern[r-self.mshp.pos[1], c-self.mshp.pos[0]]:
                            print('@', end="")
                            was_true = True
                if not was_true:
                    if self.blocks[r,c]:
                        print('#', end="")
                    else:
                        print(".", end="")
            print()

    def overlapping(self, shape):
        return np.sum(np.multiply( self.blocks[
                shape.pos[1]:shape.pos[1]+shape.height, 
                shape.pos[0]:shape.pos[0]+shape.width, 
            ], shape.pattern ))

    def step(self, change):
        if change == '<':
            self.mshp.pos[0] = max(0, min(7-self.mshp.width, self.mshp.pos[0]-1))
            if self.overlapping(self.mshp):
                self.mshp.pos[0] += 1
        elif change == '>':
            self.mshp.pos[0] = max(0, min(7-self.mshp.width, self.mshp.pos[0]+1))
            if self.overlapping(self.mshp):
                self.mshp.pos[0] -= 1
        
        if self.mshp.pos[1]-1 < 0 or self.hit_bottom(self.mshp):
            self.blocks[
                self.mshp.pos[1]:self.mshp.pos[1]+self.mshp.height, 
                self.mshp.pos[0]:self.mshp.pos[0]+self.mshp.width, 
            ] += self.mshp.pattern

            self.maxy = max(self.maxy, self.mshp.pos[1]+self.mshp.height)
            self.curshape += 1
            shp = self.shapes[self.curshape % len(self.shapes)]
            shp.pos = ara([2, self.maxy+3])
            self.mshp = shp
            self.cnt += 1
        else:
            self.mshp.pos[1] += -1

    def is_flat(self):
        return sum(self.blocks[self.maxy, :]) == 7

    def top_view(self):
        view = []
        for c in range(7):
            r = self.maxy
            while r > 0:
                if self.blocks[r, c]:
                    break
                r -= 1
            view.append(self.maxy-r)
        return tuple(view)


jetstream = sys.stdin.read().strip()

shp1 = Shape(ara([[
    1, 1, 1, 1,
]]))

shp2 = Shape(ara([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]))

shp3 = Shape(ara([
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 1],
]))

shp4 = Shape(ara([
    [1],
    [1],
    [1],
    [1]
]))

shp5 = Shape(ara([
    [1, 1],
    [1, 1]
]))


looplen = (2188-453)
dh = 2781
# looplen = (98-63)
# dh = 53

m = 1000000000000
n = m % looplen + looplen

last_height = 0
world = World(7, 3*n+6, [shp1, shp2, shp3, shp4, shp5])
world.mshp = shp1
world.mshp.pos = ara((2, 3))

lastcnt = 0
i = 0

prev = set()
prevs = {}
start = None

while world.cnt < n:
    if world.cnt != lastcnt:
        if world.is_flat():
            print("FLAT")

        state = (100000*(world.cnt % 5)+ (i % len(jetstream)), world.top_view())
        
        # if state == start:
        #     print(f"end of cnt at {world.cnt}")
        #     print(f"diff height={world.maxy-last_height}")
        #     break

        if state in prev:
            print(f"found at cnt {world.cnt} with height {world.maxy}")
            print(f'fsa {prevs[state]}')
            print(f'dh = {world.maxy-prevs[state][1]}')
            last_height = world.maxy
            start = state
            break
        
        prevs[state] = (world.cnt, world.maxy)
        prev.add( (100000*(world.cnt % 5)+ (i % len(jetstream)), world.top_view()) )
        
        lastcnt = world.cnt
    js = jetstream[i % len(jetstream)]
    world.step(js)
    i += 1


print("real", world.maxy)
print(f"looplen={looplen}")
print((m-n)/looplen)
print(f'nloops = {(m-n)//looplen}')
print(world.maxy + dh*((m-n)//looplen))