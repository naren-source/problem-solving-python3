class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insertLevelOrder(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return
        queue = [self.root]
        while True:
            currentNode = queue.pop(0)
            if currentNode.left is None:
                currentNode.left = newNode
                break
            else:
                queue.append(currentNode.left)
            if currentNode.right is None:
                currentNode.right = newNode
                break
            else:
                queue.append(currentNode.right)

    def levelOrderTraversal(self):
        queue = [self.root]
        while len(queue):
            print(queue[0].data, end=" ")
            currentNode = queue.pop(0)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

    def checkBst(self, root):
        if root.left:
            self.checkBst(root.left)
        # if not (self.minVal(root.left) < root < self.maxVal(root.right)):




bt = BinaryTree()

bt.insertLevelOrder(4)
bt.insertLevelOrder(2)
bt.insertLevelOrder(5)
bt.insertLevelOrder(1)
bt.insertLevelOrder(3)
bt.levelOrderTraversal()
print()
bt.checkBst(bt.root)

# bt.insertLevelOrder(1)
# bt.insertLevelOrder(2)
# bt.insertLevelOrder(3)
# bt.insertLevelOrder(4)
# bt.insertLevelOrder(5)
# bt.levelOrderTraversal()
# print()
# bt.checkBst()


