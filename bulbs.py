"""A wire connects N light bulbs. Each bulb has a switch associated with it; however, due to faulty wiring,
a switch also changes the state of all the bulbs to the right of the current bulb. Given an initial state of all bulbs,
find the minimum number of switches you have to press to turn on all the bulbs.
Note: 0 represents the bulb is off and 1 represents the bulb is on"""

A1 = [0, 1, 0, 1]
def bulbs(A):
    count = 0
    n = len(A)

    if n == 0:
        return count
    elif A[0] == 0:
        count = 1

    for i in range(1, len(A)):
        if A[i] == 1 and count % 2 == 1:  # count%2 = 1 means the bulbs initial value is changed
            count += 1
        elif A[i] == 0 and count % 2 == 0:
            count += 1

    return count
print(bulbs(A1))
