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
        if data < root.data:
            root.left = self.deleteMe(data, root.left)
        elif data > root.data:
            root.right = self.deleteMe(data, root.right)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                rightMinNode = self.findRightMinimum(root)
                root.data = rightMinNode.data
                root.right = self.deleteMe(root.data, root.right)
        return root

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
bst.root = bst.deleteMe(60,bst.root)
bst.inorderTraversal(bst.root)
