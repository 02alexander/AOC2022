#!/usr/bin/env python3 
import sys
import numpy as np
from collections import deque
from itertools import product

lines = sys.stdin.readlines()

def shortest_path(start, end, grid):
    visited = np.zeros_like(grid)
    nexts = deque([(start, 0, 0)])
    rows, cols = np.shape(grid)
    while nexts:
        cord, ln, prev_height = nexts.popleft()
        r, c  = cord
        if r < 0 or c < 0 or r >= rows or c >= cols:
            continue
        if not visited[r, c]:
            if grid[r, c]-prev_height <= 1:
                if cord == end:
                    return ln
                cur_height = grid[r, c]
                nexts.append(((r+1,c), ln+1, cur_height))
                nexts.append(((r,c+1), ln+1, cur_height))
                nexts.append(((r-1,c), ln+1, cur_height))
                nexts.append(((r,c-1), ln+1, cur_height))
                visited[r, c] = 1
    return None

def fastest_from_a(end, grid):
    best_time = np.ones_like(grid)*1000000000
    rows, cols = np.shape(grid)
    finish_times = []

    for start in product(range(rows), range(cols)):
        if grid[start[0], start[1]] != 1:
            continue
        
        
        nexts = deque([(start, 0, 0)])
        #print(nexts)
        rows, cols = np.shape(grid)
        #print(f"rows={rows}, cols={cols}")
        while nexts:
            cord, ln, prev_height = nexts.popleft()
            r, c  = cord
            if r < 0 or c < 0 or r >= rows or c >= cols:
                continue
            if  ln < best_time[r, c]:
                if grid[r, c]-prev_height <= 1:
                    best_time[r,c] = ln
                    if cord == end:
                        finish_times.append(ln)
                    cur_height = grid[r, c]
                    nexts.append(((r+1,c), ln+1, cur_height))
                    nexts.append(((r,c+1), ln+1, cur_height))
                    nexts.append(((r-1,c), ln+1, cur_height))
                    nexts.append(((r,c-1), ln+1, cur_height))
    return(min(finish_times))

start = None
end = None
data = []
for r, line in enumerate(lines):
    row = []
    for col, c in enumerate(line.strip()):
        if c == "S":
            start = (r, col)
            row.append(1)
        elif c == "E":
            end = (r, col)
            row.append(ord('z')-ord('a')+1)
        else:
            row.append(ord(c)-ord('a')+1)
    data.append(row)

grid = np.array(data)

print(shortest_path(start, end, grid))
print(fastest_from_a(end, grid))