# day 7
def is_valid(goal, nums, count2):
    if len(nums) == 1:
        return nums[0] == goal

    if is_valid(goal, [nums[0] + nums[1]] + nums[2:], count2):
        return True

    if is_valid(goal, [nums[0] * nums[1]] + nums[2:], count2):
        return True

    if count2 and is_valid(goal, [int(str(nums[0]) + str(nums[1]))] + nums[2:], count2):
        return True

    return False

count = 0
count2 = 0
text = open('inputs/day7_input.txt').read().strip()

for line in text.strip().split('\n'):
    goal, nums = line.strip().split(':')
    goal = int(goal)
    nums = [int(x) for x in nums.strip().split()]

    if is_valid(goal, nums, count2=False):
        count += goal
    if is_valid(goal, nums, count2=True):
        count2 += goal

print(count)
print(count2)