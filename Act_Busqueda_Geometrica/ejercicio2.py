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



points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]

tree = KDTree(points)
point_to_find = (9, 2)
nearest = find_nearest(tree.root, point_to_find)
print(f"The nearest point to {point_to_find} is {nearest}")
