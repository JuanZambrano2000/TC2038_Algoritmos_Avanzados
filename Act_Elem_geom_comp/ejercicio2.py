import matplotlib.pyplot as plt
from functools import cmp_to_key

class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

def nextToTop(S):
    return S[-2]

def distSq(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counterclockwise

def compare(p1, p2):
    o = orientation(p0, p1, p2)
    if o == 0:
        return -1 if distSq(p0, p2) >= distSq(p0, p1) else 1
    return -1 if o == 2 else 1

def convexHull(points, n):
    global p0

    ymin = points[0].y
    min = 0
    for i in range(1, n):
        y = points[i].y
        if (y < ymin) or (ymin == y and points[i].x < points[min].x):
            ymin = y
            min = i

    points[0], points[min] = points[min], points[0]

    p0 = points[0]
    sorted_points = sorted(points, key=cmp_to_key(compare))

    m = 1
    for i in range(1, n):
        while i < n - 1 and orientation(p0, sorted_points[i], sorted_points[i + 1]) == 0:
            i += 1
        sorted_points[m] = sorted_points[i]
        m += 1

    if m < 3:
        return []

    S = [sorted_points[i] for i in range(3)]

    for i in range(3, m):
        while len(S) > 1 and orientation(nextToTop(S), S[-1], sorted_points[i]) != 2:
            S.pop()
        S.append(sorted_points[i])

    return S

# New input points
input_points = [(-19, -17), (-15, 3), (-12, 11), (-8, -5), (-7, 14), (-3, -9), (-1, 0 ),
                (2, 18), (4, -13), (6, 7), (9, -16), (11, 5), (13, -2), (16, 12), (18, -7),
                (-20, 6), (-14, -18), (-9, 9), (-4, -12), (-2, 15), (1, -14), (3, 10),
                (7, -8), (12, 19), (17, -4)]

points = [Point(p[0], p[1]) for p in input_points]
n = len(points)
hull_points = convexHull(points, n)

# Plotting
plt.figure(figsize=(10, 8))
plt.scatter(*zip(*input_points), color='blue')  # plot points

# Plot the hull
if hull_points:
    for i in range(len(hull_points)):
        plt.plot([hull_points[i].x, hull_points[(i + 1) % len(hull_points)].x],
                 [hull_points[i].y, hull_points[(i + 1) % len(hull_points)].y],
                 color='red')

plt.title('Points and their Convex Hull using Graham\'s Scan')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
