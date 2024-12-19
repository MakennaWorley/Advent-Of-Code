# day 4
def within_array(x, y):
    return 0 <= x < len(text) and 0 <= y < len(text[0])


def count_in_direction(x, y, dx, dy):
    word = "XMAS"
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if not within_array(nx, ny) or text[nx][ny] != word[i]:
            return 0
    return 1


directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]
count = 0
count2 = 0
text = []

with open('inputs/day4_input.txt', 'r') as file:
    for line in file:
        text.append(line.strip())
    file.close()

for i in range(len(text)):
    for j in range(len(text[0])):
        for dx, dy in directions:
            count += count_in_direction(i, j, dx, dy)

R = len(text)
C = len(text[0])

for r in range(R):
    for c in range(C):
        if r + 2 < R and c + 2 < C and text[r][c] == 'M' and text[r + 1][c + 1] == 'A' and text[r + 2][c + 2] == 'S' and text[r + 2][c] == 'M' and text[r][c + 2] == 'S':
            count2 += 1
        if r + 2 < R and c + 2 < C and text[r][c] == 'M' and text[r + 1][c + 1] == 'A' and text[r + 2][c + 2] == 'S' and text[r + 2][c] == 'S' and text[r][c + 2] == 'M':
            count2 += 1
        if r + 2 < R and c + 2 < C and text[r][c] == 'S' and text[r + 1][c + 1] == 'A' and text[r + 2][c + 2] == 'M' and text[r + 2][c] == 'M' and text[r][c + 2] == 'S':
            count2 += 1
        if r + 2 < R and c + 2 < C and text[r][c] == 'S' and text[r + 1][c + 1] == 'A' and text[r + 2][c + 2] == 'M' and text[r + 2][c] == 'S' and text[r][c + 2] == 'M':
            count2 += 1

print(count)
print(count2)