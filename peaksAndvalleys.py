a = [1,8,6,2,3,4,6]

def peaksAndValleys1(A):
    """First we sort array and then sway every 2 elements, incrementing +2, take examples and verify"""
    A.sort()
    for i in range(1, len(A)-1, 2):
        temp = A[i]
        A[i] = A[i+1]
        A[i+1] = temp

    return A
# to-do
def peaksAndValleys2(A):
    pass

print(peaksAndValleys1(a))
