# day 12
from collections import deque

DIRECTIONS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left
count = 0
count2 = 0

text = open('inputs/day12_input.txt').read().strip()

field = text.split('\n')
row = len(field)
column = len(field[0])

SEEN = set()
for r in range(row):
    for c in range(column):
        if (r,c) in SEEN:
            continue

        Q = deque([(r,c)])
        area = 0
        perim = 0
        PERIM = dict()

        while Q:
            r2,c2 = Q.popleft()
            if (r2,c2) in SEEN:
                continue

            SEEN.add((r2,c2))
            area += 1
            for dr,dc in DIRECTIONS:
                rr = r2+dr
                cc = c2+dc

                if 0<=rr<row and 0<=cc<column and field[rr][cc]==field[r2][c2]:
                    Q.append((rr,cc))

                else:
                    perim += 1

                    if (dr,dc) not in PERIM:
                        PERIM[(dr,dc)] = set()

                    PERIM[(dr,dc)].add((r2,c2))

        sides = 0
        for k,vs in PERIM.items():
            SEEN_PERIM = set()
            old_sides = sides

            for (pr,pc) in vs:
                if (pr,pc) not in SEEN_PERIM:
                    sides += 1
                    Q = deque([(pr,pc)])

                    while Q:
                        r2,c2 = Q.popleft()
                        if (r2,c2) in SEEN_PERIM:
                            continue

                        SEEN_PERIM.add((r2,c2))
                        for dr,dc in DIRECTIONS:
                            rr,cc = r2+dr,c2+dc

                            if (rr,cc) in vs:
                                Q.append((rr,cc))

        count += area*perim
        count2 += area*sides

print(count)
print(count2)