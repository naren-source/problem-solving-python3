class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.i = 0

    def nth_reverse(self, head, position):
        self.i=0
        if head is None:
            return
        self.nth_reverse(head.next, position)
        self.i+=1
        if self.i == position:
            print(head.data)


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

oLinkedList.nth_reverse(oLinkedList.head, 2)
