# no of leaders program, an element in array is said to be leader if the element is strictly greater than all
# elements on the right side
a = [10, 7, 9, 3, 5, 2, 4, ]
n = len(a)
mx = a[n-1]
c = 1
for i in range(n-2, -1, -1):
    if a[i] > mx:
        mx = a[i]
        c += 1
print(c)
