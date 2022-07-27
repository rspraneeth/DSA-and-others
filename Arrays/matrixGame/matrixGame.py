def matGame():
    """Approach: As we observe, any element can be accessed by using a formula. a[i][j] = (i*m)+j+1.
    So we take a row array and col array and use the values as rows and columns respectively. An example would help."""
    n, m, Q = map(int, input('Enter n, m, q: ').split())
    r, c = [], []
    for i in range(n):
        r.append(i)
    for i in range(m):
        c.append(i)

    for i in range(Q):
        q = list(map(int, input('Enter operation and parameters: ').split()))
        t = q[0]
        if t == 1:
            c1 = q[1] - 1
            c2 = q[2] - 1
            temp = c[c1]
            c[c1] = c[c2]
            c[c2] = temp
        elif t == 2:
            r1 = q[1] - 1
            r2 = q[2] - 1
            temp = r[r1]
            r[r1] = r[r2]
            r[r2] = temp
        elif t == 3 or t == 4:
            x1 = q[1] - 1
            y1 = q[2] - 1
            x2 = q[3] - 1
            y2 = q[4] - 1
            x = r[x1] * m + c[y1] + 1
            y = r[x2] * m + c[y2] + 1
            if t == 3:
                print(x | y)
            else:
                print(x & y)
    return 0

matGame()
