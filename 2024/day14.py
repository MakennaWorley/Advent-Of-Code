# day 14
import re
from collections import deque

DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left

def ints(s):
    return [int(x) for x in re.findall(r'-?\d+', s)]

count = 0
count2 = 0
D = open('inputs/day14_input.txt').read().strip()

X = 101
Y = 103
q1 = 0
q2 = 0
q3 = 0
q4 = 0

robots = []

for line in D.split('\n'):
    px,py,vx,vy = ints(line)
    robots.append((px,py,vx,vy))

for t in range(1,10**6):
    G = [['.' for x in range(X)] for y in range(Y)]
    if t==100:
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        mx = X//2
        my = Y//2

    for i,(px,py,vx,vy) in enumerate(robots):
        px += vx
        py += vy
        px %= X
        py %= Y
        robots[i] = (px, py, vx, vy)
        assert 0<=px<X
        assert 0<=py<Y
        G[py][px] = '#'

        if t==100:
            if px<mx and py<my:
                q1 += 1
            if px>mx and py<my:
                q2 += 1
            if px<mx and py>my:
                q3 += 1
            if px>mx and py>my:
                q4 += 1
    if t==100:
        # part 1
        print(q1*q2*q3*q4)

    components = 0
    SEEN = set()
    for x in range(X):
        for y in range(Y):
            if G[y][x] == '#' and (x,y) not in SEEN:
                sx,sy = x,y
                components += 1
                Q = deque([(sx,sy)])

                while Q:
                    x2,y2 = Q.popleft()
                    if (x2,y2) in SEEN:
                        continue

                    SEEN.add((x2,y2))
                    for dx,dy in DIRS:
                        xx,yy = x2+dx,y2+dy
                        if 0<=xx<X and 0<=yy<Y and G[yy][xx]=='#':
                            Q.append((xx,yy))

    if components <= 200:
        print(t)
        gstr = []
        for row in G:
            gstr.append(''.join(row))

        print('\n'.join(gstr))
        break