class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def searchItr(self, value):
        looper = self.head
        while(value != looper.data):
            looper = looper.next
            if looper == None:
                return False
        return True

    def searchRec(self, head, value):
        if head == None:
            return False
        if head.data == value:
            return True
        return self.searchRec(head.next, value)


oLL = LinkedList()
node1 = Node(1)
oLL.head = node1
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
print(oLL.searchItr(int(input())))
print(oLL.searchRec(oLL.head, int(input())))
