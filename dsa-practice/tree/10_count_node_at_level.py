class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def countNodesAtLevel(self, root, targetLevel):
        queue = [(root, 0)]
        countNodes = 0
        while queue:
            node, level = queue.pop(0)
            if level == targetLevel:
                countNodes += 1
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return countNodes


tree = Tree()
root = Node(1)
tree.root = root
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(tree.countNodesAtLevel(tree.root, 2))
