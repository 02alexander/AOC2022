#!/usr/bin/env python3 
import sys
from collections import defaultdict
import os.path
import pathlib

lines = sys.stdin.readlines()
#inp = sys.stdin.read()

i = 0
cwd = "/"
dirs = defaultdict(set)
while i < (len(lines)):
    l = lines[i].strip()
    print(l)
    print(cwd)
    toks = l.split()
    if toks[0] == '$':
        if toks[1] == 'ls':
            i += 1
            print("running ls")
            while i < (len(lines)) and  lines[i][0] != '0':
                nl = lines[i].strip()
                ntoks = nl.split()
                if ntoks[0] == 'dir':
                    print(f'add dir {cwd+ntoks[1]}')
                    dirs[str(cwd)].add(cwd+ntoks[1]+"/")
                elif ntoks[0][0].isnumeric():
                    print(f' add file {(int(ntoks[0]), ntoks[1])} ')
                    dirs[str(cwd)].add((int(ntoks[0]), ntoks[1]))
                else:
                    print(f'break {nl}')
                    i -= 1
                    break
                #dirs[l].add()
                i += 1
        elif toks[1] == "cd":
            if toks[2] == "..":
                cwd = os.path.dirname(cwd)
                if cwd != "/":
                    cwd += "/"
            elif toks[2] == "/":
                cwd = "/"
            else:
                cwd += f"{toks[2]}/"
    else:
        print("ERROR")
        break

    i += 1

def sz(p):
    global dirs
    sm = 0
    for child in dirs[p]:
        if type(child) is tuple:
            sm += child[0]
        else:
            sm += sz(child)
    return sm

print()
count = 0
for d in list(dirs.keys()):
    s = sz(d)
    if s <= 100000:
        print(d)
        count += s
print()
print(dirs.keys())

print(count)
