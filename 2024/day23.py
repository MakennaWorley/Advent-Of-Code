# day 23
from collections import defaultdict
import random

text = open('inputs/day23_input.txt').read().strip()

dict = defaultdict(set)
for line in text.split('\n'):
    a,b, = line.split('-')
    dict[a].add(b)
    dict[b].add(a)

xs = sorted(dict.keys())

count = 0
for i,a in enumerate(xs):
    for j in range(i+1, len(xs)):
        for k in range(j+1, len(xs)):
            b = xs[j]
            c = xs[k]
            if a in dict[b] and a in dict[c] and b in dict[c]:
                if a.startswith('t') or b.startswith('t') or c.startswith('t'):
                    count += 1

print(count)

best = None

for t in range(1000):
    random.shuffle(xs)
    clique = []
    for x in xs:
        ok = True
        for y in clique:
            if x not in dict[y]:
                ok = False

        if ok:
            clique.append(x)

    if best is None or len(clique) > len(best):
        best = clique

print(','.join(sorted(best)))