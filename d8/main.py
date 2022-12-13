#!/usr/bin/env python3 
import sys
import numpy as np

lines = sys.stdin.read().strip().splitlines()
#inp = sys.stdin.read()

heights = []
for line in lines:
    cl = []
    for c in line:
        cl.append(ord(c)-ord('0'))
    heights.append(cl)


def visibles(row):
    visible_indices = []
    cur_max = -100000000 # count outer
    for i, d in enumerate(row):
        if d > cur_max:
            visible_indices.append(i)
        cur_max = max(cur_max, d)
    return np.array(visible_indices)

def count_below_max(row, mx):
    count = 0
    cur_max = mx
    for i, d in enumerate(row):
        if d < cur_max:
            count += 1
        else:
            count += 1
            break
    return count

def viewing_distance(row, idx):
    return (count_below_max(list(reversed(row[:idx])), row[idx]),
            count_below_max(row[idx+1:], row[idx]),       
    )

def dists(heights, r, c):
    return viewing_distance(heights[:,c], r)+viewing_distance(heights[r,:], c)

def ss(heights, r, c):
    distances = dists(heights, r, c)
    h = heights[r,c]
    return np.prod(list(distances))

heights = np.array(heights)
vis = np.zeros_like(heights)
rows, cols  = heights.shape

mx = 0
best_spot = None
for r in range(rows):
    for c in range(cols):
        scenic_score = ss(heights, r, c)
        if scenic_score > mx:
            best_spot = (r, c)
            print("new_best", scenic_score)
        mx = max(mx, scenic_score)

# print(heights)
# print(heights[2, :])
# print("dfzgzf", viewing_distance(heights[2,:], 1))
# print(viewing_distance(heights[:, 1], 2))

# print()

# print()
print()
print(dists(heights, 1,2))
print(viewing_distance(heights[:,2], 1))
print(viewing_distance(heights[1,:], 2))
print()
print(best_spot)
print(mx)

# print(rows*cols)
# print(heights)
# for r in range(len(lines[0])):

#     # print(visibles(heights[r, :]))
    
#     for i in visibles(heights[r,:]):
#         vis[r, i] = 1
    
#     #print(list(reversed(heights[r,:])))
#     #print(visibles(list(reversed(heights[r,:]))))
    
#     for i in visibles(list(reversed(heights[r,:]))):
#         vis[r, rows-1-i] = 1


#     for i in visibles(heights[:,r]):
#         vis[i, r] = 1

#     for i in visibles(list(reversed(heights[:,r]))):
#         vis[rows-1-i, r] = 1




    

# print(vis)


# print(np.sum(vis))
