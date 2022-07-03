# Given an array find the length of the smallest sub array, which contains both min and max of the array
a = [2, 2, 6, 4, 5, 1, 5, 1, 2, 6, 4, 3, 4, 1]
n = len(a)
mx = max(a)
mn = min(a)
min_len = n
mxi = -1
mni = -1
if mx == mn:
    min_len = 1
# else:
#     for i in range(n):
#         if a[i] == mx:
#             for j in range(i+1, n):
#                 if a[j] == mx:
#                     break
#                 if a[j] == mn:
#                     min_len = min(j-i+1, min_len)  # len = j-i+1
#                     break
#         elif a[i] == mn:
#             for j in range(i+1, n):
#                 if a[j] == mn:
#                     break
#                 if a[j] == mx:
#                     min_len = min(j-i+1, min_len)
#                     break

else:  # from right to left
    for i in range(n - 1, -1, -1):
        if a[i] == mx:
            mxi = i
            if mni != -1:
                len = mni - mxi + 1
                min_len = min(len, min_len)
        elif a[i] == mn:
            mni = i
            if mxi != -1:
                len = mxi - mni + 1
                min_len = min(len, min_len)

print(min_len)
