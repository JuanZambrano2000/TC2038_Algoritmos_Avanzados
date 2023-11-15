import matplotlib.pyplot as plt
import math

def draw_line(point1, point2):
  plt.plot([point1[0], point2[0]], [point1[1], point2[1]])

def line_intersection(line1, line2):
  xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
  ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

  def det(a, b):
      return a[0] * b[1] - a[1] * b[0]

  div = det(xdiff, ydiff)
  if div == 0:
     raise Exception('lines do not intersect')

  d = (det(*line1), det(*line2))
  x = det(d, xdiff) / div
  y = det(d, ydiff) / div
  return x, y

def line_angle(line):
  return math.atan2(line[1][1] - line[0][1], line[1][0] - line[0][0])

points = [(5,2), (3,2), (-2.3,1.2), (-2,-2), (3,4), (10,1), (2,5), (3,4), (5,8), (-7.3,3.5), (14.4,-14.4), (8,7), (3,3), (-1,-1), (2,5), (5.4,-3.1)]

for i in range(0, len(points), 2):
  draw_line(points[i], points[i+1])

plt.show()

for i in range(0, len(points), 2):
  for j in range(i+2, len(points), 2):
      intersection = line_intersection((points[i], points[i+1]), (points[j], points[j+1]))
      print(f"Intersection of line {i} and {j}: {intersection}")
      angle1 = line_angle((points[i], points[i+1]))
      angle2 = line_angle((points[j], points[j+1]))
      angle_diff = abs(angle1 - angle2)
      print(f"Angle difference between line {i} and {j}: {math.degrees(angle_diff)} degrees")
