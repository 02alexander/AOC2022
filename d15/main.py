#!/usr/bin/env python3

import sys
import re
lines = sys.stdin.readlines()

class Sensor:
    def __init__(self, line):
        words = line.split()
        self.x = int(words[2][2:-1])
        self.y = int(words[3][2:-1])
        self.beaconx = int(words[8][2:-1])
        self.beacony = int(words[9][2:])
        self.dist = abs( self.x-self.beaconx )+abs(self.beacony-self.y)
    def range_row(self, y):
        dy = abs(self.y-y)
        length = self.dist-dy
        if length < 0:
            return None
        if dy != 0:
            return (self.x-length, self.x+length, (self.y-y)//dy)
        return (self.x-length, self.x+length, 1)

def check_row(y, ranges, lm):
    cnt = 0
    biggest_x = 0
    lastsx = 0
    for (sx, ex, dr) in ranges:
        ex = min(lm, ex)
        if biggest_x is None:
            cnt += ex+1-sx
            lastsx = sx
            biggest_x = ex
        if ex > biggest_x:
            if sx <= biggest_x:
                cnt += ex-biggest_x
            else:
                cnt += ex+1-sx
            biggest_x = ex

    occ = set()
    for sensor in sensors:
        if sensor.beacony == y and sensor.beacony not in occ:
            occ.add(sensor.beacony)
        if sensor.y == y and sensor.y not in occ:
            occ.add(sensor.y)
    return cnt

def is_alternating(ranges):
    last = 2
    for i in range(len(ranges)-1):
        if ranges[i][2] == last:
            return False
        last = ranges[i][2]
    return True


y = 0
lm = 4000000
#lm = 20
while y < lm:

    sensors = []
    ranges = []
    for line in lines:
        sensor = Sensor(line)
        sensors.append(sensor)
        r = sensor.range_row(y)
        if r:
            ranges.append(r)

    ranges.sort()
    n = check_row(y, ranges, lm)
    if n != lm:
        mxx = 0
        for i in range(len(ranges)):
            if ranges[i][0]-1> mxx:
                print(y, ranges[i][0]-1)
                xm = 4000000
                x = ranges[i][0]-1
                print(x*xm+y)
                sys.exit(0)
            mxx = max(mxx, ranges[i][1])

    minln = 1000000000
    if is_alternating(ranges):
        for r in ranges:
            minln = min(minln, (r[1]-r[0])//2)
            minln = min(abs(r[0]), minln )
            minln = min(abs(r[1]-lm), minln )
    else:
        for i in range(len(ranges)-1):
            if ranges[i+1][2] != ranges[i][2]:
                minln = min( (min(ranges[i+1][0], ranges[i][1])-ranges[i][0])//2, minln )
            else:
                minln = min(abs(ranges[i+1][0]-ranges[i][1])//2, minln)


    if minln <= 1:
        y += 1
    else:
        y += minln-1
            
