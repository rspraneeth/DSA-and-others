a = [1, 2, 3, 4, 5, 1, 2, 3, 5, 2, 1, 2, 3, 4, 2, 1, 2, 3, 4, 2, 1, 2, 4, 5, 1, 1, 2, 3]
print(a)
b = {}  # a hash map b is declared
for i in a:  # to find the freq of an element in arr a
    if i in b.keys():
        b[i] += 1
    else:
        b[i] = 1
print(b)
b[6] = 3  # inserting a new value
b[7] = 4
print(b)
b[7] = 6  # updating the value of a key
print(b)
del b[7]  # deleting a pair
print(b)
b.pop(6)  # deleting a pair
print(b)
