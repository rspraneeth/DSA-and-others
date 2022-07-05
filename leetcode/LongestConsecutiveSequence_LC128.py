arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

def longestConsecutive(nums):
    """Approach is by checking the previous number not in set, that means we can start a consecutive sequence elements
    as long as next element is in set"""
    nums = set(nums)
    consec_len = 0
    for num in nums:
        if num - 1 not in nums:  # checking if previous num is not in set
            ln = 1
            while num + 1 in nums:  # we will check for consecutive elements, until the element is not in set
                ln += 1
                num += 1
            consec_len = max(consec_len, ln)

    return consec_len

print(longestConsecutive(arr))
# TC: O(n), the if condition prevents to enter the while loop when previous num is present in set and
# the while loop inside checks only when next num is in set. While loop runs for only n times in the code.
# This optimizes total time. Take examples and check
