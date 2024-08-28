class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def deleteFromStart(self):
        first = self.head
        self.head = self.head.next
        first = None


    def deleteFromEnd(self):
        looper = self.head
        prevNode = None
        while(looper.next):
            prevNode = looper
            looper = looper.next
        looper = None
        prevNode.next = None


    def deleteFromPos(self, position):
        looper = self.head
        prevNode = None
        while(position>1):
            position -= 1
            prevNode = looper
            looper = looper.next
        prevNode.next = looper.next
        looper = None

    def deleteThisNode(self, node: Node):
        looper = self.head
        prevNode = None
        while(looper != node):
            prevNode = looper
            looper = looper.next
        if prevNode is None:
            self.head = self.head.next
        else:
            prevNode.next = looper.next
            looper = None

    def printLL(self):
        looper = self.head
        while(looper):
            print(looper.data, end="")
            looper = looper.next


oLinkedList = LinkedList()

node1 = Node(1)
oLinkedList.head = node1
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5
node6 = Node(6)
node5.next = node6

oLinkedList.deleteFromStart()
oLinkedList.printLL()
print()

oLinkedList.deleteFromEnd()
oLinkedList.printLL()
print()

oLinkedList.deleteFromPos(3)
oLinkedList.printLL()
print()

oLinkedList.deleteThisNode(node3)
oLinkedList.printLL()
print()

