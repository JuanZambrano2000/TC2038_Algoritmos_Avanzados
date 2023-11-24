import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, point, left=None, right=None):
        self.point = point  # the point in 2D space
        self.left = left    # left child
        self.right = right  # right child

class KDTree:
    def __init__(self, points):
        self.root = self.build(points, depth=0)

    def build(self, points, depth):
        if not points:
            return None

        # Alternate between x and y axis
        axis = depth % 2

        # Sort point list and choose median as pivot element
        points.sort(key=lambda x: x[axis])
        median = len(points) // 2

        # Create node and construct subtrees
        return Node(
            point=points[median],
            left=self.build(points[:median], depth + 1),
            right=self.build(points[median + 1:], depth + 1)
        )

def find_nearest(tree, point, depth=0, best=None):
    if tree is None:
        return best

    axis = depth % 2

    # Update best if this point is closer
    if best is None or distance_squared(point, tree.point) < distance_squared(point, best):
        best = tree.point

    # Check subtrees; start with the side of the split the point is on
    next_branch = tree.left if point[axis] < tree.point[axis] else tree.right
    opposite_branch = tree.right if point[axis] < tree.point[axis] else tree.left

    best = find_nearest(next_branch, point, depth + 1, best)

    # Check if we need to check the opposite side
    if distance_to_axis(point, tree.point, axis) < distance_squared(point, best):
        best = find_nearest(opposite_branch, point, depth + 1, best)

    return best

def distance_squared(point1, point2):
    return sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2))

def distance_to_axis(point, tree_point, axis):
    return (point[axis] - tree_point[axis]) ** 2

def is_within_ranges(point, x_ranges, y_ranges):
    """Check if a point is within the specified x and y ranges."""
    x, y = point
    return any(x_min <= x <= x_max for x_min, x_max in x_ranges) and \
           any(y_min <= y <= y_max for y_min, y_max in y_ranges)

'''
points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]

tree = KDTree(points)
point_to_find = (9, 2)
nearest = find_nearest(tree.root, point_to_find)
print(f"The nearest point to {point_to_find} is {nearest}")
'''
#Provided by chatgpt

# Generate 200 random points
points = [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(200)]

# Create the KD Tree
tree = KDTree(points)

# Define search points
search_points_x = [(-1, 1), (-2, 1), (-7, 0), (-2, 2), (-7, 5)]
search_points_y = [(-2, 2), (3, 5), (-6, 4), (-3, 3), (-3, 1)]

# Find nearest points
nearest_points_x = [find_nearest(tree.root, p) for p in search_points_x]
nearest_points_y = [find_nearest(tree.root, p) for p in search_points_y]

# Plotting
plt.figure(figsize=(10, 10))
plt.scatter(*zip(*points), color='blue', label='Original Points')
plt.scatter(*zip(*search_points_x), color='red', marker='x', label='Search Points X-axis')
plt.scatter(*zip(*search_points_y), color='green', marker='x', label='Search Points Y-axis')
plt.scatter(*zip(*nearest_points_x), color='red', label='Nearest Points X-axis')
plt.scatter(*zip(*nearest_points_y), color='green', label='Nearest Points Y-axis')

# Adding x-axis and y-axis
plt.axhline(0, color='black',linewidth=0.8)
plt.axvline(0, color='black',linewidth=0.8)

plt.title('KD Tree Nearest Neighbor Search')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)
plt.legend()
plt.show()

# Find points within the specified ranges
points_within_ranges = [p for p in points if is_within_ranges(p, search_points_x, search_points_y)]

# Plotting
plt.figure(figsize=(10, 10))
plt.scatter(*zip(*points), color='blue', label='Original Points')
plt.scatter(*zip(*points_within_ranges), color='orange', label='Points Within Ranges')
plt.scatter(*zip(*search_points_x), color='red', marker='x', label='Search Points X-axis')
plt.scatter(*zip(*search_points_y), color='green', marker='x', label='Search Points Y-axis')

# Adding x-axis and y-axis
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.title('Points Within Specified Ranges')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)
plt.legend()
plt.show()
