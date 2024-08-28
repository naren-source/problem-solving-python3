class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class OriginalStack:
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
        self.size -= 1
        return popEl.data

    def __str__(self):
        peeper = self.head.next
        stackString = "Stack: "
        while(peeper):
            stackString += str(peeper.data) + "->"
            peeper = peeper.next
        return stackString


class QStack:
    def __init__(self):
        self.stackOne = OriginalStack()
        self.stackTwo = OriginalStack()

    def push(self, data):
        if self.stackOne.isEmpty():
            self.stackTwo.push(data)
        else:
            self.stackOne.push(data)

        print(f"One {self.stackOne}")
        print(f"Two {self.stackTwo}")

    def pop(self):
        if self.stackOne.isEmpty():
            self.shiftStack(self.stackTwo, self.stackOne)
            self.stackOne.pop()
            self.shiftStack(self.stackOne, self.stackTwo)
        else:
            self.shiftStack(self.stackOne, self.stackTwo)
            self.stackOne.pop()
            self.shiftStack(self.stackTwo, self.stackOne)

        print(f"One {self.stackOne}")
        print(f"Two {self.stackTwo}")

    def shiftStack(self, s1, s2):
        while not s1.isEmpty():
            s2.push(s1.pop())

    def __str__(self):
        queue = "Queue: "
        rStack1 = self.stackOne
        rStack2 = self.stackTwo

        if self.stackOne.isEmpty():
            rStack1 = self.stackTwo
            rStack2 = self.stackOne

        self.shiftStack(rStack1, rStack2)
        while not rStack2.isEmpty():
            queue += str(rStack2.peep()) + "*"
            rStack1.push(rStack2.pop())

        return queue


stack = QStack()

stack.push(1)
stack.push(2)
print(stack)
print()

stack.pop()
print(stack)
print()

stack.push(3)
print(stack)
print()

stack.push(4)
stack.pop()
print(stack)
print()

stack.push(5)
print(stack)
print()
