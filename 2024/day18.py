# day 18
from collections import deque

DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left

ans = 0
text = open('inputs/day18_input.txt').read().strip()

N = 71
G = [['.' for c in range(N)] for r in range(N)]

for i,line in enumerate(text.split('\n')):
    x,y = [int(x) for x in line.split(',')]
    if 0<=y<N and 0<=x<N:
        G[y][x] = '#'

    queue = deque([(0,0,0)])
    visited = set()
    ok = False

    while queue:
        d,r,c = queue.popleft()
        if (r,c) == (N-1,N-1):
            if i==1023:
                print(d)

            ok = True
            break

        if (r,c) in visited:
            continue

        visited.add((r,c))
        for dr,dc in DIRS:
            rr = r+dr
            cc = c+dc
            if 0<=rr<N and 0<=cc<N and G[rr][cc] != '#':
                queue.append((d+1,rr,cc))

    if not ok:
        print(f'{x},{y}')
        break