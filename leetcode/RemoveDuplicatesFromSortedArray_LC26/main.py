A = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

def removeDuplicates(nums):
    n = len(nums)
    k = 1  # k is index of final array, starting from 1 because 0 will be always be in final array
    for i in range(1, n):
        if nums[i] != nums[i - 1]:  # since nums is sorted, if prev != curr, then prev and curr are non-decrsng sequence
            nums[k] = nums[i]  # whenever cond is true, then we change nums with curr with index respective to k
            k += 1

    return k, nums[:k]

print(removeDuplicates(A))
