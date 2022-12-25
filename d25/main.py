#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def tobase(n, b):
    digits = []
    while n:
        digits.append(n % b)
        n = n//5
    return digits[::-1]
        
 
def to_snafu(dec):
    hept = tobase(dec, 5)
    hept = list(reversed(hept))+[0]
    for i in range(len(hept)):
        if hept[i] == 3:
            hept[i] = '='
            hept[i+1] += 1
        elif hept[i] == 4:
            hept[i] = '-'
            hept[i+1] += 1
        else:
            if hept[i] == 5:
                hept[i] = 0
                hept[i+1] += 1
    print(hept)
    return hept

totsum = 0
for line in lines:
    sm = 0
    for e, ch in enumerate(reversed(line.strip())):
        
        if ch == '-':
            d = -1
        elif ch == '=':
            d = -2
        else:
            d = int(ch)
        #kprint(e, d)
        sm += 5**e*d
    print(sm)
    totsum += sm

print(''.join(map(str,reversed(to_snafu(totsum)))))
# 33038276688955
# 2-=2==00-0==2=022=10