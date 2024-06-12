class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorderStackTraversal(self):
        stack = []
        currentNode = self.root
        while True:
            if currentNode is not None:
                stack.append(currentNode)
                currentNode = currentNode.left
            elif stack:
                currentNode = stack.pop()
                print(currentNode.data, end=" ")
                currentNode = currentNode.right
            else:
                break
        print()

    def morrisTraversal(self):
        pass

bt = BinaryTree()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

bt.root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

bt.inorderStackTraversal()
bt.morrisTraversal()
