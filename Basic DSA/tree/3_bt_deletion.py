class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def deleteNode(self, data):
        queue = [self.root]
        dNode = None
        currentNode = None
        while len(queue):
            currentNode = queue.pop(0)
            if currentNode.data == data:
                dNode = currentNode
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        dNode.data = currentNode.data
        self.deleteDeepestNode(currentNode)

    def deleteDeepestNode(self, deepNode):
        queue = [self.root]
        while len(queue):
            currentNode = queue.pop(0)
            if currentNode.left:
                if currentNode.left is deepNode:
                    currentNode.left = None
                    break
                else:
                    queue.append(currentNode.left)
            if currentNode.right:
                if currentNode.right is deepNode:
                    currentNode.right = None
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

bt.levelOrderTraversal()
print()
bt.deleteNode(2)
bt.levelOrderTraversal()
