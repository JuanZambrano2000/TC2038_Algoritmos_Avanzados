import random # To generate random values

class RangeTreeNode:
    def __init__(self, low, high, value, left=None, right=None):
        self.low = low
        self.high = high
        self.value = value
        self.left = left
        self.right = right

    def find_split_node(self, value):
        if value < self.value:
            if self.left is None:
                return self
            else:
                return self.left.find_split_node(value)
        elif value > self.value:
            if self.right is None:
                return self
            else:
                return self.right.find_split_node(value)
        else:
            return self

    def values_in_range(self, low, high):
        # List to store values within the range
        values = []

        # If the current node is within the range, add its value
        if low <= self.value <= high:
            values.append(self.value)

        # If the left child exists and the range intersects with its range, traverse left
        if self.left is not None and low <= self.left.high:
            values.extend(self.left.values_in_range(low, high))

        # If the right child exists and the range intersects with its range, traverse right
        if self.right is not None and high >= self.right.low:
            values.extend(self.right.values_in_range(low, high))

        return values

def build_range_tree(values):
    if not values:
        return None

    values = sorted(values)  # Make sure values are sorted
    median_index = len(values) // 2
    median_value = values[median_index]

    left_values = values[:median_index]
    right_values = values[median_index + 1:]

    left_node = build_range_tree(left_values)
    right_node = build_range_tree(right_values)

    return RangeTreeNode(min(values), max(values), median_value, left_node, right_node)
'''
values = [5, 2, 4, 1, 3]

range_tree = build_range_tree(values)

values_in_range = range_tree.values_in_range(2, 6)
print("Values in range 2-6:", values_in_range)
'''

random_values = [random.randint(-10, 10) for _ in range(2000)]
range_tree = build_range_tree(random_values)

values_in_range = [(-1,-0.5),(2,4),(-5,-4),(-10,-9.3),(9,9.5)]
for i in range(len(values_in_range)):
    print("Values in range", values_in_range[i], ":", range_tree.values_in_range(values_in_range[i][0], values_in_range[i][1]))