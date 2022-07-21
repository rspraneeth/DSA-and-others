import math

points1 = [[1, 3], [3, 3], [5, 3], [2, 2]]
queries1 = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]

def countPoints(points, queries):
    ans = []
    for c in queries:
        s = 0
        for p in points:
            d = math.sqrt((p[0] - c[0]) ** 2 + (p[1] - c[1]) ** 2)
            if d <= c[2]:
                s += 1
        ans.append(s)
    return ans

print(countPoints(points1, queries1))

# 1828. Queries on Number of Points Inside a Circle
# You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane.
# Multiple points can have the same coordinates. You are also given an array queries where
# queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.
# For each query queries[j], compute the number of points inside the jth circle.
# Points on the border of the circle are considered inside.
# Return an array answer, where answer[j] is the answer to the jth query.
