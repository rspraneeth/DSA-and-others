# Given an array A of non-negative integers, arrange them such that they form the largest number.
# Return a string representing the largest number.
from functools import cmp_to_key

arr = [3, 2, 34, 5, 6, 7, 5, 4]

def largestNumber(A):
    A = list(map(str, A))  # changing int list to str list using map()

    def compare(x, y):
        if x + y > y + x:  # concatenating x, y and checking which integer value is greater, need not use int(x+y).
            return -1
        else:
            return 1

    A = sorted(A, key=cmp_to_key(compare))
    if A[0] == '0':  # this means array consists of only zeros, so the first element is 0 after sorting.
        return 0  # concatenating all the 0's in array gives value like '000000' but we need '0'
    return ''.join(A)

print(largestNumber(arr))

# Sorting all numbers in descending order is the simplest solution that occurs to us. But this doesn't work.
# For example, 548 is greater than 60, but in the output, 60 comes before 548. As a second example, 98 is greater
# than 9, but 9 comes before 98 in the output. The solution is to use any comparison-based sorting algorithm.
# Thus, instead of using the default comparison, write a comparison function myCompare() and use it to sort numbers.
# Given two numbers, X and Y, how should myCompare() decide which number to put first –
# we compare two numbers XY (Y appended at the end of X) and YX (X appended at the end of Y).
# If XY is greater, then, in the output, X should come before Y, else Y should come before X.
# For example, let X and Y be 542 and 60. To compare X and Y, we compare 54260 and 60542.
# Since 60542 is greater than 54260, we put Y first.
