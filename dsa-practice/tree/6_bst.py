class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertNode(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            self.insertMe(newNode, self.root)

    def insertMe(self, node, root):
        if node.data < root.data:
            if root.left is None:
                root.left = node
                return
            self.insertMe(node, root.left)
        else:
            if root.right is None:
                root.right = node
                return
            self.insertMe(node, root.right)

    def deleteMe(self, data, root):
        pass
    def findRightMinimum(self, root):
        while root.left:
            root = root.left
        return root

    def searchMe(self, data, root):
        if  root is None or root.data == data:
            return root
        if data < root.data:
            return self.searchMe(data, root.left)
        else:
            return self.searchMe(data, root.right)

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.data, end=" ")
            self.inorderTraversal(root.right)


bst = BinarySearchTree()
bst.insertNode(50)
bst.insertNode(30)
bst.insertNode(20)
bst.insertNode(40)
bst.insertNode(70)
bst.insertNode(60)
bst.insertNode(80)
bst.inorderTraversal(bst.root)
print()
print(
    (bst.searchMe(60, bst.root)).data if bst.searchMe(60, bst.root) \
        else False
)
print(
    (bst.searchMe(90, bst.root)).data if bst.searchMe(90, bst.root) \
        else False
)
