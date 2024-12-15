# day 15
from collections import deque

def solve(graph,part2):
    row = len(graph)
    column = len(graph[0])
    graph = [[graph[r][c] for c in range(column)] for r in range(row)]

    if part2:
        big_graph = []
        for r in range(row):
            temp_graph = []
            for c in range(column):
                if graph[r][c] == '#':
                    temp_graph.append('#')
                    temp_graph.append('#')

                if graph[r][c] == 'O':
                    temp_graph.append('[')
                    temp_graph.append(']')

                if graph[r][c] == '.':
                    temp_graph.append('.')
                    temp_graph.append('.')

                if graph[r][c] == '@':
                    temp_graph.append('@')
                    temp_graph.append('.')
                    
            big_graph.append(temp_graph)

        graph = big_graph
        column *= 2

    for r in range(row):
        for c in range(column):
            if graph[r][c] == '@':
                sr,sc = r,c
                graph[r][c] = '.'

    r,c = sr,sc
    for inst in instructions:
        if inst == '\n':
            continue

        dr,dc = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}[inst]
        rr,cc = r+dr,c+dc
        if graph[rr][cc]=='#':
            continue

        elif graph[rr][cc]=='.':
            r,c = rr,cc

        elif graph[rr][cc] in ['[', ']', 'O']:
            Q = deque([(r,c)])
            SEEN = set()
            ok = True

            while Q:
                rr,cc = Q.popleft()
                if (rr,cc) in SEEN:
                    continue

                SEEN.add((rr,cc))
                rrr,ccc = rr+dr, cc+dc
                if graph[rrr][ccc]=='#':
                    ok = False
                    break

                if graph[rrr][ccc] == 'O':
                    Q.append((rrr,ccc))

                if graph[rrr][ccc]=='[':
                    Q.append((rrr,ccc))
                    assert graph[rrr][ccc+1]==']'
                    Q.append((rrr,ccc+1))

                if graph[rrr][ccc]==']':
                    Q.append((rrr,ccc))
                    assert graph[rrr][ccc-1]=='['
                    Q.append((rrr,ccc-1))

            if not ok:
                continue

            while len(SEEN) > 0:
                for rr,cc in sorted(SEEN):
                    rrr,ccc = rr+dr,cc+dc
                    if (rrr,ccc) not in SEEN:
                        assert graph[rrr][ccc] == '.'
                        graph[rrr][ccc] = graph[rr][cc]
                        graph[rr][cc] = '.'
                        SEEN.remove((rr,cc))
            r = r+dr
            c = c+dc

    ans = 0
    for r in range(row):
        for c in range(column):
            if graph[r][c] in ['[', 'O']:
                ans += 100*r+c
    return ans

D = open('inputs/day15_input.txt').read().strip()

graph, instructions = D.split('\n\n')
graph = graph.split('\n')

print(solve(graph, False))
print(solve(graph, True))