ch = ['b', 'a', 'a', 'g', 'd', 'c', 'a', 'g', 'g']
# find no pairs (ij) 'ag' exists and i<j
# basic approach, iterating from left to right
# c = 0
# for i in range(len(ch)):
#     if ch[i] == 'a':
#         for j in range(i+1, len(ch)):
#             if ch[j] == 'g':
#                 c += 1
# print(c)

# optimized approach, iterating from right to left, carry forwarding count of 'g' and adding to 'a'
# ans,c = 0, 0
# for i in range(len(ch)-1, -1, -1):
#     if ch[i] == 'g':
#         c += 1
#     elif ch[i] == 'a':
#         ans += c
# print(ans)

# iterating from left to right, carry forwarding count of 'a' and adding to 'g'
ans, c = 0, 0
for i in range(len(ch)):
    if ch[i] == 'a':
        c += 1
    elif ch[i] == 'g':
        ans += c
print(ans)


# your blind approach, but tried to reduce iterations, but why did I do this!!! such a big code, try the smarter way
# def g_exists(ch, count):
#     if 'g' not in ch:
#         return count
#     else:
#         count += 1
#         j = ch.index('g')
#         return g_exists(ch[j + 1:], count)
#
# c = 0
# cnt = 0
# exists = True
#
# while exists:
#     if 'a' in ch:
#         i = ch.index('a')
#         ch = ch[i+1:]
#     else:
#         exists = False
#     if exists and 'g' in ch:
#         c = 1
#         j = ch.index('g')
#         cnt += g_exists(ch[j+1:], c)
#
#     else:
#         exists = False
#
# print(cnt)
