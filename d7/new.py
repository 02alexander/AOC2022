#!/usr/bin/env python3 
import sys

lines = sys.stdin.readlines()
#inp = sys.stdin.read()

class Node:
    def __init__(self, parent=None):
        self.files = []
        self.children = {}
        self.name = ""
        self.parent = self
        if parent:
            self.parent = parent

    def __str__(self):
        return f"{self.files} ; {[str(c).strip() for c in self.children.values()]}"
        


root = Node()
root.name = "/"
cur_node = root
in_ls = True
for line in lines:
    toks = line.strip().split()
    if toks[0] == ("$"):
        in_ls = False
        if toks[1] == "cd":
            if toks[2] == "..":
                #print(str(cur_node))
                cur_node = cur_node.parent
            elif toks[2] == "/":
                cur_node = root
            else:
                cur_node = cur_node.children[toks[2]]
        if toks[1] == "ls":
            in_ls = True
    elif in_ls and toks[0] == "dir":
        cur_node.children[toks[1]] = Node(cur_node)
        cur_node.children[toks[1]].name = toks[1]
    elif toks[0][0].isnumeric():
        cur_node.files.append((toks[1], int(toks[0])))
    else:
        print(str(root))
        print("ERORR")
        break


nodes = []
def traverse(node):
    global nodes
    nodes.append(node)
    for child in node.children.values():
        traverse(child)

def sz(node):
    sm = 0
    for file in node.files:
        sm += file[1]
    for child in node.children.values():
        sm += sz(child)
    return sm

traverse(root)

sm = 0
for node in nodes:
    s = sz(node)
    if s < 100000:
        sm += s
print(sm)

tot_space = 70000000
needed = 30000000-(tot_space-sz(root))
print("needed=", needed)

smallest = 2349082093482034
for node in nodes:
    s = sz(node)
    if s >= needed:
        smallest = min(smallest, s)

print(smallest)