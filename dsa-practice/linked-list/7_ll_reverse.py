class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        looper = self.head
        while(looper):
            print(looper.data, end=" ")
            looper = looper.next

    def reverseList(self, head, prevNode = None):
        if head is None:
            self.head = prevNode
            return
        self.reverseList(head.next, head)
        head.next = prevNode

    def reverseListItr(self):
        prevNode = None
        currentNode = self.head
        while(currentNode):
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        self.head = prevNode

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

oLinkedList.printList()
print()
# oLinkedList.reverseList(oLinkedList.head)
oLinkedList.reverseListItr()
oLinkedList.printList()
