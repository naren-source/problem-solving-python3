class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, newNode: Node):
        newNode.next = self.head
        self.head = newNode

    def insertAtPos(self, position: int, newNode: Node):
        looper = self.head
        position -= 1
        while(position>1):
            looper = looper.next
            position -= 1
        newNode.next = looper.next
        looper.next = newNode

    def insertAfter(self, afterNode: Node, newNode: Node):
        newNode.next = afterNode.next
        afterNode.next = newNode

    def insertAtEnd(self, newNode: Node):
        looper = self.head
        while(looper.next):
            looper = looper.next
        looper.next = newNode

    def printLL(self):
        looper = self.head
        while(looper):
            print(looper.data, end=" ")
            looper = looper.next


oLinkedList = LinkedList()

node1 = Node(2)
node2 = Node(5)
node3 = Node(7)
oLinkedList.head = node1
node1.next = node2
node2.next = node3

oLinkedList.printLL()
print()

newNode = Node(10)
oLinkedList.insertAtStart(newNode)
oLinkedList.printLL()
print()

newNode = Node(15)
oLinkedList.insertAtPos(3, newNode)
oLinkedList.printLL()
print()

newNode1 = Node(20)
oLinkedList.insertAfter(newNode, newNode1)
oLinkedList.printLL()
print()

newNode = Node(25)
oLinkedList.insertAtEnd(newNode)
oLinkedList.printLL()
print()
