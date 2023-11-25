import matplotlib.pyplot as plt
import math
import random

# Draw a line segment using plot function
def draw_line(point1, point2, color):
    plt.plot([point1[0], point2[0]], [point1[1], point2[1]], color=color)
    plt.scatter([point1[0], point2[0]], [point1[1], point2[1]], color=color)  # Marking the points

# https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
def line_intersection(line1, line2):
    # Diference between X and Y coordinates of the two lines
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
    # Determinant of the two points
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]
    
    div = det(xdiff, ydiff)
    if div == 0:
        # lines do not intersect
        return None  
    # Computing the intersection 
    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def line_angle(line1, line2):
    def angle(line):
        return math.atan2(line[1][1] - line[0][1], line[1][0] - line[0][0])

    ang1 = angle(line1)
    ang2 = angle(line2)
    ang_diff = math.degrees(abs(ang1 - ang2))
    return min(ang_diff, 360 - ang_diff)  # Return the smaller angle of intersection

# Line Segments
lines = [
    ((5, 2), (3, 2)),
    ((-2, 3), (1, 2)),
    ((-2, -2), (3, 4)),
    ((10, 1), (2, 5)),
    ((3, 4), (5, 8)),
    ((-7, 3), (3, 5)),
    ((14, 4), (-14, 4)),
    ((8, 7), (3, 3)),
    ((-1, -1), (2, 5)),
    ((5, 4), (-3, 1))
]

plt.figure(figsize=(10, 8))

# Generate a random color for each line chatGPT
colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(len(lines))]

# Draw the lines with different colors
for i, line in enumerate(lines):
    draw_line(line[0], line[1], colors[i])

# Calculate and display intersections and angles
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        intersection = line_intersection(lines[i], lines[j])
        if intersection:
            print(f"Intersection of line {i+1} and {j+1}: {intersection}")
            angle = line_angle(lines[i], lines[j])
            print(f"Angle of intersection between line {i+1} and {j+1}: {angle} degrees")

plt.title('Line segments')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
