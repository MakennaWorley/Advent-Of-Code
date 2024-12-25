# day 25
def fits(key, lock):
    R = len(key)
    assert R == len(lock)
    C = len(key[0])
    assert C == len(lock[0])
    for r in range(R):
        for c in range(C):
            if key[r][c]=='#' and lock[r][c]=='#':
                return False
    return True


text = open('inputs/day25_input.txt').read().strip()

shapes = text.split('\n\n')
keys = []
locks = []

for shape in shapes:
    G = shape.split('\n')
    R = len(G)
    C = len(G[0])
    G = [[G[r][c] for c in range(C)] for r in range(R)]
    is_key = True

    for c in range(C):
        if G[0][c] == '#':
            is_key = False

    if is_key:
        keys.append(shape)

    else:
        locks.append(shape)

count = 0
for key in keys:
    for lock in locks:
        if fits(key, lock):
            count += 1
            
print(count)