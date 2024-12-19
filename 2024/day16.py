# day 16
import heapq

DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left

ans = 0
text = open('inputs/day16_input.txt').read().strip()

graph = text.split('\n')
row = len(graph)
column = len(graph[0])
graph = [[graph[r][c] for c in range(column)] for r in range(row)]

for r in range(row):
    for c in range(column):
        if graph[r][c] == 'S':
            sr,sc = r,c
        if graph[r][c] == 'E':
            er,ec = r,c

queue = []
SEEN = set()
heapq.heappush(queue, (0,sr,sc,1))
DIST = {}
best = None
while queue:
    d,r,c,dir = heapq.heappop(queue)
    if (r,c,dir) not in DIST:
        DIST[(r,c,dir)] = d

    if r==er and c==ec and best is None:
        best = d

    if (r,c,dir) in SEEN:
        continue

    SEEN.add((r,c,dir))
    dr,dc = DIRS[dir]
    rr,cc = r+dr,c+dc
    if 0<=cc<column and 0<=rr<row and graph[rr][cc] != '#':
        heapq.heappush(queue, (d+1, rr,cc,dir))

    heapq.heappush(queue, (d+1000, r,c,(dir+1)%4))
    heapq.heappush(queue, (d+1000, r,c,(dir+3)%4))
print(best)

queue = []
SEEN = set()
for dir in range(4):
    heapq.heappush(queue, (0,er,ec,dir))

DIST2 = {}
while queue:
    d,r,c,dir = heapq.heappop(queue)
    if (r,c,dir) not in DIST2:
        DIST2[(r,c,dir)] = d

    if (r,c,dir) in SEEN:
        continue

    SEEN.add((r,c,dir))
    dr,dc = DIRS[(dir+2)%4]
    rr,cc = r+dr,c+dc
    if 0<=cc<column and 0<=rr<row and graph[rr][cc] != '#':
        heapq.heappush(queue, (d+1, rr,cc,dir))

    heapq.heappush(queue, (d+1000, r,c,(dir+1)%4))
    heapq.heappush(queue, (d+1000, r,c,(dir+3)%4))

OK = set()
for r in range(row):
    for c in range(column):
        for dir in range(4):
            if (r,c,dir) in DIST and (r,c,dir) in DIST2 and DIST[(r,c,dir)] + DIST2[(r,c,dir)] == best:
                OK.add((r,c))

print(len(OK))
