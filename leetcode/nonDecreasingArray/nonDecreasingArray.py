ls = [4,2,3,6]
def checkPossibility(nums):
    n = len(nums)
    check = 0  # to check if an element is modified
    for i in range(1, n):
        if nums[i-1] > nums[i]:  # checking for any decreasing sequence
            if check == 1:  # will return false if we modified an element once
                return False
            check += 1  # if an element in array is not modified then increase check
            # if prev of prev of curr is less than or equal to curr, then we make the greater equal to lesser (prev = curr).
            if i == 1 or nums[i-2] <= nums[i]:  # i == 1 means nums[0]>nums[1]
                nums[i-1] = nums[i]
            else:  # if prev of prev is greater than curr then we have to make the lesser equal to greater (curr = prev)
                nums[i] = nums[i-1]
    return True

print(checkPossibility(ls))
