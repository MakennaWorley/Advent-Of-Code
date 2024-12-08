# day 8
from collections import defaultdict

count = 0
count2 = 0

graph = open('inputs/day8_input.txt').read().strip().split('\n')

row_len = len(graph)
col_len = len(graph[0])

dict = defaultdict(list)

for r in range(row_len):
    for c in range(col_len):
        if graph[r][c] != '.':
            dict[graph[r][c]].append((r,c))

antinode = set()
antinode2 = set()

for row in range(row_len):
    for col in range(col_len):
        for _,values in dict.items():

            for (r1,c1) in values:
                for (r2,c2) in values:
                    if (r1,c1) == (r2,c2):
                        continue

                    d1 = abs(row-r1)+abs(col-c1)
                    d2 = abs(row-r2)+abs(col-c2)

                    dr1 = row-r1
                    dr2 = row-r2
                    dc1 = col-c1
                    dc2 = col-c2

                    if (d1==2*d2 or d1*2==d2) and 0<=row<row_len and 0<=col<col_len and (dr1*dc2 == dc1*dr2):
                        antinode.add((row,col))
                    if 0<=row<row_len and 0<=col<col_len and (dr1*dc2 == dc1*dr2):
                        antinode2.add((row,col))

count = len(antinode)
count2 = len(antinode2)

print(count)
print(count2)