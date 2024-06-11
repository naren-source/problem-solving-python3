class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("top")
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peep(self):
        return self.head.next.data

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head.next
        self.head.next = newNode
        self.size += 1

    def pop(self):
        popEl = self.head.next
        self.head.next = popEl.next
        popEl = None
        self.size -= 1

    def __str__(self):
        peeper = self.head.next
        stackString = ""
        while(peeper):
            stackString += str(peeper.data) + " "
            peeper = peeper.next
        return stackString


stack = Stack()
print(stack.isEmpty())
stack.push(1)
print(stack.isEmpty())
print(stack)
stack.push(2)
stack.pop()
print(stack)
print(stack.peep())
stack.push(3)
print(stack)
print(stack.getSize())
stack.push(4)
stack.push(5)
print(stack)
