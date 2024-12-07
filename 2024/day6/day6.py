# day 6
count = 0
count2 = 0
text = open('day6_input.txt').read().strip()

row_change = [-1, 0, 1, 0]
column_change = [0, 1, 0, -1]
start_x, start_y = 0, 0

graph = text.split('\n')
R = len(graph)
C = len(graph[0])

for r in range(R):
    for c in range(C):
        if graph[r][c] == '^':
            start_x, start_y = r, c

for o_r in range(R):
    for o_c in range(C):
        r, c = start_x, start_y
        d = 0
        visited = set()
        unique = set()

        while True:
            if (r, c, d) in visited:
                count2 += 1
                break

            visited.add((r, c, d))
            unique.add((r, c))

            new_r = r + row_change[d]
            new_c = c + column_change[d]

            if not (0 <= new_r < R and 0 <= new_c < C):
                if graph[o_r][o_c] == '#':
                    count = len(unique)
                break

            if graph[new_r][new_c] == '#' or (new_r == o_r and new_c == o_c):
                d = (d + 1) % 4
            else:
                r = new_r
                c = new_c

print(count)
print(count2)
