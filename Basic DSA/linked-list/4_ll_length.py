class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def length_itr(self):
        count = 0
        looper = self.head
        while(looper):
            count += 1
            looper = looper.next
        return count

    def length_recursize(self, head):
        if not head:
            return 0
        return 1 + self.length_recursize(head.next)

    def length_recursize_constant(self, head, count=0):
        if not head:
            return count
        return self.length_recursize_constant(head.next, count+1)


oLinkedList = LinkedList()
node1 = Node(1)
oLinkedList.head = node1
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4

print(oLinkedList.length_itr())
print(oLinkedList.length_recursize(oLinkedList.head))
print(oLinkedList.length_recursize_constant(oLinkedList.head))
