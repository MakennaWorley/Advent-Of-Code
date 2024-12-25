# day 20
from collections import deque

def find_cheat(d0, columnHEAT_TIME):
    ans = set()
    queue = deque([(0,None,None,None,sr,sc)])
    SEEN = set()
    SAVE = 100

    while queue:
        d,cheat_start,cheat_end,cheat_time,r,c = queue.popleft()
        assert cheat_end is None
        if d>=d0-SAVE:
            continue

        if graph[r][c] == 'E':
            if cheat_end is None:
                cheat_end = (r,c)

            if d<=d0-SAVE and (cheat_start,cheat_end) not in ans:
                ans.add((cheat_start, cheat_end))

        if (r,c,cheat_start,cheat_end,cheat_time) in SEEN:
            continue

        SEEN.add((r,c,cheat_start,cheat_end,cheat_time))

        if cheat_start is None:
            assert graph[r][c] != '#'
            queue.append((d,(r,c),None,columnHEAT_TIME,r,c))

        if cheat_time is not None and graph[r][c]!='#':
            assert graph[r][c] in ['.', 'S', 'E']
            if DIST[(r,c)] <= d0-100-d:
                ans.add((cheat_start, (r,c)))

        if cheat_time == 0:
            continue

        else:
            for dr,dc in DIRS:
                rr,cc = r+dr, c+dc
                if cheat_time is not None:
                    assert cheat_time > 0
                    if 0<=rr<row and 0<=cc<column:
                        queue.append((d+1,cheat_start,None,cheat_time-1,rr,cc))

                else:
                    if 0<=rr<row and 0<=cc<column and graph[rr][cc]!='#':
                        queue.append((d+1,cheat_start,cheat_end,cheat_time,rr,cc))

    return len(ans)


DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left

ans = 0
text = open('inputs/day20_input.txt').read().strip()

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

DIST = {}
queue = deque([(0,er,ec)])

while queue:
    d,r,c = queue.popleft()
    if (r,c) in DIST:
        continue

    DIST[(r,c)] = d
    for dr,dc in DIRS:
        rr,cc = r+dr, c+dc
        if 0<=rr<row and 0<=cc<column and graph[rr][cc]!='#':
            queue.append((d+1,rr,cc))

d0 = DIST[(sr,sc)]

print(find_cheat(d0, 2))
print(find_cheat(d0, 20))