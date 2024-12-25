# day 19
def ways(words, target):
    if target in dict:
        return dict[target]

    ans = 0
    if not target:
        ans = 1

    for word in words:
        if target.startswith(word):
            ans += ways(words, target[len(word):])

    dict[target] = ans
    return ans


count = 0
count2 = 0

text = open('inputs/day19_input.txt').read().strip()
words, targets = text.split('\n\n')
words = words.split(', ')

dict = {}
for target in targets.split('\n'):
    target_ways = ways(words, target)
    if target_ways > 0:
        count += 1

    count2 += target_ways

print(count)
print(count2)