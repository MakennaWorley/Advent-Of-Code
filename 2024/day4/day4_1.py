# day 4: puzzle 1
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
text = []

with open('2024/day4/day4_input.txt', 'r') as file:
    for line in file:
        text.append(line.strip())
    file.close()

for i in range(len(text)):
    for j in range(len(text[0])):
        for dx, dy in directions:
            count += count_in_direction(i, j, dx, dy)

print(count)