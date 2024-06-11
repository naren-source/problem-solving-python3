# Basic linked list creation and traversal

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


vLinkedList = LinkedList()
node1 = Node(2)
node2 = Node(4)
node3 = Node(6)
vLinkedList.head = node1
node1.next = node2
node2.next = node3
vLinkedList.printList()

