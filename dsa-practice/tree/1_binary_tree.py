class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def levelorder(self, root):
        queue = [root]
        while len(queue):
            print(queue[0].data, end=" ")
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
bt = BinaryTree()
bt.root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node4.right = node8
node2.right = node5
node3.left = node6
node3.right = node7
bt.inorder(bt.root)
print()
bt.preorder(bt.root)
print()
bt.postorder(bt.root)
print()
bt.levelorder(bt.root)
print()
