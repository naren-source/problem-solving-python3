class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def morrisTraversal(self):
        current = self.root
        while current:
            if current.left is None:
                print(current.data, end=" ")
                current = current.right
            else:
                leftSubTree = current.left
                while leftSubTree.right and leftSubTree.right != current:
                    leftSubTree = leftSubTree.right

                if leftSubTree.right is None:
                    leftSubTree.right = current
                    current = current.left
                elif leftSubTree.right == current:
                    leftSubTree.right = None
                    print(current.data, end=" ")
                    current = current.right


tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)
tree.morrisTraversal()

#         1
#     2           3
# 4       5           6

#   4 2 5 1 3 6
