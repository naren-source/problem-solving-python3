class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorderTraversal(self, root):
        if root is None: return
        self.inorderTraversal(root.left)
        print(root.data, end=" ")
        self.inorderTraversal(root.right)

    def storeInorder(self, root, tempArr):
        if root is None: return
        self.storeInorder(root.left, tempArr)
        tempArr.append(root.data)
        self.storeInorder(root.right, tempArr)

    def bstConvert(self, root, tempArr):
        if root is None: return
        self.bstConvert(root.left, tempArr)
        root.data = tempArr[0]
        tempArr.pop(0)
        self.bstConvert(root.right, tempArr)

    def btToBst(self, root):
        tempArr = []
        self.storeInorder(root, tempArr)
        tempArr.sort()
        self.bstConvert(root, tempArr)

bt = BinaryTree()
bt.root = Node(10)
bt.root.left = Node(30)
bt.root.right = Node(15)
bt.root.left.left = Node(20)
bt.root.right.right = Node(5)
bt.inorderTraversal(bt.root)
print()
bt.btToBst(bt.root)
bt.inorderTraversal(bt.root)

