# find first non repeating element in array

a = [1, 2, 3, 4, 5, 1, 2, 3, 5, 2, 1, 2, 6, 3, 4, 2, 1, 2, 3, 4, 2, 1, 2, 4, 5, 1, 1, 2, 3, 0]
print(a)
b = {}  # a hash map b is declared
for i in a:  # to find the freq of an element in arr a
    if i in b.keys():
        b[i] += 1
    else:
        b[i] = 1
print(b)
for i in a:
    if b[i] == 1:  # if the freq of an element is one means it is non repeating.
        print(i)
        break

for i in b:  # the latest python release has ordered hashmaps(order of the array passed)
    if b[i] == 1:
        print(i)
        break
