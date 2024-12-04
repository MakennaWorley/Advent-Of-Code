# day 4: puzzle 2
text = []

with open('2024/day4/day4_input.txt', 'r') as file:
    for line in file:
        text.append(line.strip())
    file.close()

count = 0

R = len(text)
C = len(text[0])

for r in range(R):
    for c in range(C):
        if r + 2 < R and c + 2 < C and text[r][c] == 'M' and text[r + 1][c + 1] == 'A' and text[r + 2][c + 2] == 'S' and text[r + 2][c] == 'M' and text[r][c + 2] == 'S':
            count += 1
        if r + 2 < R and c + 2 < C and text[r][c] == 'M' and text[r + 1][c + 1] == 'A' and text[r + 2][c + 2] == 'S' and text[r + 2][c] == 'S' and text[r][c + 2] == 'M':
            count += 1
        if r + 2 < R and c + 2 < C and text[r][c] == 'S' and text[r + 1][c + 1] == 'A' and text[r + 2][c + 2] == 'M' and text[r + 2][c] == 'M' and text[r][c + 2] == 'S':
            count += 1
        if r + 2 < R and c + 2 < C and text[r][c] == 'S' and text[r + 1][c + 1] == 'A' and text[r + 2][c + 2] == 'M' and text[r + 2][c] == 'S' and text[r][c + 2] == 'M':
            count += 1

print(count)
