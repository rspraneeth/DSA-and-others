ar = [1, 2, 3, 4, 5]
n = len(ar)
pf = [0] * n
pf[0] = ar[0]
fsmp = 0
smp = 0
for i in range(1, n):
    pf[i] = pf[i - 1] + ar[i]
print(pf)
for i in range(n):
    sm = 0
    for j in range(i, n):
        print([ar[i] for i in range(i, j + 1)])  # printing all sub arrays O(n**3)
        sum = 0
        for k in range(i, j + 1):
            sum = sum + ar[k]  # printing sum of each sub array O(n**3)
        print(sum)
        if i == 0:  # printing the sum of each sub array using prefix sum array, so O(n**2)
            print(pf[j])
        else:
            print(pf[j] - pf[i - 1])

        sm += ar[j]  # sum of each sub array using carry forward
        print(sm)
        smp += sm  # total sum of sum of sub arrays
        # if ar[i] == 2:  # printing sum of sum of sub array for a particular value, similarly we can find total sum of sum
        #     smp += sm  # sum of sum of each sub array, still takes O(n**2)
        # fsmp += smp  # if value '2' is present more than once then we need to add for every i = 2

print(smp)

# sum of a sub array means total sum of values present in that sub array that means
# total sum of sum of each sub array = multiplying the value with no of sub arrays of that value gives sum of that
# value present in each sub array , eg: in the given array 1 is present in 6 sub arrays only, that means total sum of 1
# in all sub arrays is 6*1 = 6, similarly calculating for every value and adding them gives total sum of sum of sub arrays
t_sum = 0
for i in range(n):
    left = i + 1  # no of ele's present on right side of index including index
    right = n - i  # no of ele's present on right side of index including index
    no_of_sub = left * right
    print(f"In {no_of_sub} sub arrays value {ar[i]} is present")  # in how many sub arrays ar[i] is present
    t_sum += no_of_sub * ar[i]  # multiplying the value with no of sub arrays of that value and adding all sums
print(t_sum)
