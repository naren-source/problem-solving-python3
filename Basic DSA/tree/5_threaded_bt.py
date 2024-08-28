class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.threadFlag = False

class ThreadedBinaryTree:
    def __init__(self):
        self.root = None

    def insertTNodeOrdered(self, data):
        newnode = TNode(data)

        if self.root is None:
            self.root = newnode
            return

        currentNode = self.root
        while currentNode:
            if data < currentNode.data:
                if currentNode.left is None:
                    newnode.right = currentNode
                    currentNode.left = newnode
                    newnode.threadFlag = True
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.threadFlag:
                    currentNode.threadFlag = False
                    newnode.right = currentNode.right
                    currentNode.right = newnode
                    newnode.threadFlag = True
                    break
                elif currentNode.right is None:
                    currentNode.right = newnode
                    break
                else:
                    currentNode = currentNode.right

    def insertTNodeUnordered(self, data):
        newnode = TNode(data)
        if self.root is None:
            self.root = newnode
            return
        queue = [self.root]
        while len(queue):
            currentNode = queue.pop(0)
            if currentNode.left:
                queue.append(currentNode.left)
            else:
                currentNode.left = newnode
                newnode.right = currentNode
                newnode.threadFlag = True
                break
            if currentNode.right:
                if currentNode.threadFlag:
                    currentNode.threadFlag = False
                    newnode.right = currentNode.right
                    currentNode.right = newnode
                    newnode.threadFlag = True
                    break
                else:
                    queue.append(currentNode.right)
            else:
                currentNode.right = newnode
                break

    def inorderTraversal(self):
        currentNode = self.leftMostNode(self.root)
        while currentNode:
            print(currentNode.data, end=" ")
            if currentNode.threadFlag:
                currentNode = currentNode.right
            else:
                currentNode = self.leftMostNode(currentNode.right)

    def leftMostNode(self, node):
        if not node:
            return None
        while node.left:
            node = node.left
        return node


tbt = ThreadedBinaryTree()

# tbt.insertTNodeOrdered(20)
# tbt.insertTNodeOrdered(10)
# tbt.insertTNodeOrdered(30)
# tbt.insertTNodeOrdered(5)
# tbt.insertTNodeOrdered(15)
# tbt.insertTNodeOrdered(25)
# tbt.insertTNodeOrdered(35)

tbt.insertTNodeUnordered(20)
tbt.insertTNodeUnordered(15)
tbt.insertTNodeUnordered(25)
tbt.insertTNodeUnordered(35)
tbt.insertTNodeUnordered(10)
tbt.insertTNodeUnordered(30)
tbt.insertTNodeUnordered(5)


tbt.inorderTraversal()

#Ordered
# 20
# 10 30
# 5 15 25 35

#Unordered
# 20
# 15 25
# 35 10 30 5
