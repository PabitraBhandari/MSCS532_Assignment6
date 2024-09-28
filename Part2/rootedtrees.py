# Tree Node Implementation
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List of child nodes
    
    def add_child(self, child_node):
        self.children.append(child_node)  # Add child node to the tree
    
    def traverse(self):
        print(self.value, end=": ")
        for child in self.children:
            print(child.value, end=" ")
        print()
        for child in self.children:
            child.traverse()

# Example Usage:
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)

root.add_child(child1)
root.add_child(child2)
child1.add_child(TreeNode(4))
child2.add_child(TreeNode(5))

root.traverse()
# Output:
# 1: 2 3
# 2: 4
# 3: 5
