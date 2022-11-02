class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self, value):
        self.head = self.current = Node(value)

    def enqueue(self, val):
        self.current.next = Node(val)
        self.current = self.current.next

    def removeHead(self):
        self.head = self.head.next

    def removeLast(self):
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None

    def display(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

queue = Queue(50)
queue.enqueue(14)
queue.enqueue(19)
queue.removeLast()
queue.display()