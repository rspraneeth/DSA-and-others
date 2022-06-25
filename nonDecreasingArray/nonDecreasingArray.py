ls = [4,2,3,6]
def checkPossibility(nums):
    n = len(nums)
    check = 0
    for i in range(1, n):
        if nums[i-1] > nums[i]:
            if check == 1:
                return False
            check += 1
            if i == 1 or nums[i-2] <= nums[i]:
                nums[i-1] = nums[i]
            else:
                nums[i] = nums[i-1]
    return True

print(checkPossibility(ls))
