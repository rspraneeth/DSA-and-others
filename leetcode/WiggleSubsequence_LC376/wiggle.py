A = [1,17,5,10,13,15,10,5,16,8]

def wiggleMaxLength1(nums):
    n = len(nums)
    ln = 0  # to calculate length of sequence of +ve, -ve, +ve, -ve,......

    if n == 0:
        return 0
    elif n == 1:
        return 1

    cdf = nums[1] - nums[0]  # current difference
    if cdf > 0:
        pos_pvdf = True  # positive previous difference.
        ln = 1
    elif cdf < 0:
        pos_pvdf = False
        ln = 1

        # we haven't considered cdf == 0 condition, so ln will remain same(ln = 0). Same applies in 'for' loop.

    for i in range(2, n):
        cdf = nums[i] - nums[i - 1]
        if cdf > 0:
            if ln == 0:  # checking if first 2 elements cdf=0 in array
                ln = 1
            elif not pos_pvdf:  # if cdf positive and pvdf negative then we increase ln
                ln += 1
            pos_pvdf = True
        elif cdf < 0:
            if ln == 0:
                ln = 1
            elif pos_pvdf:
                ln += 1
            pos_pvdf = False
        # whenever cdf = 0 comes in this 'for' loop, ln value remains same.

    return ln + 1  # we are taking '+1' because we calculated length of sequence, but the array has ln + 1(take examples and check)

def wiggleMaxLength2(nums):
    inc = 1  # increasing
    dec = 1  # decreasing
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 0:
            inc = dec + 1
        elif nums[i] - nums[i-1] < 0:
            dec = inc + 1
    return min(len(nums), max(inc, dec))


print(wiggleMaxLength1(A))
print(wiggleMaxLength2(A))
