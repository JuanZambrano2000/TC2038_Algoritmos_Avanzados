class RangeTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.subtree_values = []

class RangeTree:
    def __init__(self, values):
        self.root = self.build_tree(sorted(values))

    def build_tree(self, values):
        if not values:
            return None
        
        mid = len(values) // 2
        node = RangeTreeNode(values[mid])
        node.left = self.build_tree(values[:mid])
        node.right = self.build_tree(values[mid+1:])
        node.subtree_values = values
        return node

    # Method to find the split node
    def find_split_node(self, root, low, high):
        node = root
        while node and not (low <= node.value <= high):
            if low < node.value:
                node = node.left
            else:
                node = node.right
        return node

    # Method to report values in range
    def values_in_range(self, root, low, high):
        def report_subtree(node):
            if node:
                for value in node.subtree_values:
                    if low <= value <= high:
                        result.append(value)

        result = []
        split_node = self.find_split_node(root, low, high)

        if split_node is None:
            return result

        # Traverse the left side from the split node
        if split_node.value >= low:
            node = split_node.left
            while node:
                if low <= node.value:
                    report_subtree(node.right)
                    node = node.left
                else:
                    node = node.right

        # Traverse the right side from the split node
        if split_node.value <= high:
            node = split_node.right
            while node:
                if high >= node.value:
                    report_subtree(node.left)
                    node = node.right
                else:
                    node = node.left

        # Add split node value if it's in range
        if low <= split_node.value <= high:
            result.append(split_node.value)

        return result

values = [1, 3, 5, 7, 9, 11]
tree = RangeTree(values)
print(tree.values_in_range(tree.root, 4, 10))  # This will return [5, 7,