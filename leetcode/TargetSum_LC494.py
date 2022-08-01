from functools import cache

n1 = [1, 1, 1, 1, 1]
t1 = 3
# both the approaches are using caching
def findTargetSumWays(nums, target):
    @cache
    def bt(i, s):
        if i == len(nums):
            return (0, 1)[s == target]
        return bt(i + 1, s + nums[i]) + bt(i + 1, s - nums[i])

    return bt(0, 0)

def findTargetSumWays1(nums, target):
    dp = {}

    def bt(i, s):
        if i == len(nums):
            return (0, 1)[s == target]
        if (i, s) in dp:
            return dp[(i, s)]
        dp[(i, s)] = (bt(i + 1, s + nums[i])) + (bt(i + 1, s - nums[i]))
        return dp[(i, s)]

    return bt(0, 0)

print(findTargetSumWays(n1, t1))
print(findTargetSumWays1(n1, t1))

# Leet code: 494. Target Sum
# You are given an integer array nums and an integer target. You want to build an expression out of nums by
# adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build
# the expression "+2-1". Return the number of different expressions that you can build, which evaluates to target
