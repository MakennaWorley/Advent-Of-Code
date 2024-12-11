# day 10
from collections import deque
def ways1(sr,sc):
    queue = deque([(sr,sc)])
    ans = 0
    SEEN = set()
    while queue:
        r,c = queue.popleft()
        if (r,c) in SEEN:
            continue
        SEEN.add((r,c))
        if graph[r][c]==0:
            ans += 1
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = r+dr
            cc = c+dc
            if 0<=rr<row and 0<=cc<column and graph[rr][cc] == graph[r][c]-1:
                queue.append((rr,cc))
    return ans

def ways(r,c):
    if graph[r][c]==0:
        return 1
    if (r,c) in dict:
        return dict[(r,c)]
    ans = 0
    for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
        rr = r+dr
        cc = c+dc
        if 0<=rr<row and 0<=cc<column and graph[rr][cc] == graph[r][c]-1:
            ans += ways(rr,cc)
    dict[(r,c)] = ans
    return ans

count = 0
count2 = 0
text = open('inputs/day10_input.txt').read().strip()

graph = text.split('\n')
graph = [[int(x) for x in row] for row in graph]
row = len(graph)
column = len(graph[0])
dict = {}

for r in range(row):
    for c in range(column):
        if graph[r][c]==9:
            count += ways1(r,c)
            count2 += ways(r,c)

print(count)
print(count2)