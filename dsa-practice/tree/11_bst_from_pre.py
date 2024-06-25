class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BT:
    def __init__(self):
        self.root = None

    def constructBST(self, data, root):
        if self.root is None:
            self.root = Node(data)
        else:
            if data < root.data:
                if root.left is None:
                    root.left = Node(data)
                else:
                    self.constructBST(data, root.left)
            else:
                if root.right is None:
                    root.right = Node(data)
                else:
                    self.constructBST(data, root.right)

    def inOrderTraversal(self, root):
        if root is None:
            return
        self.inOrderTraversal(root.left)
        print(root.data, end=" ")
        self.inOrderTraversal(root.right)

bt = BT()
preOrder = [10, 5, 1, 7, 40, 50]
for pre in preOrder:
    bt.constructBST(pre, bt.root)
bt.inOrderTraversal(bt.root)

# 1 5 7 10 40 50

#     10
#  5     40
# 1 7       50

# 1 7 5 50 40 10

