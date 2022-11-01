class Node:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode


class MyLinkedList:
    def __init__(self):
        dummy = Node(0)
        self.head = dummy
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head
        for i in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:  # Invalid index
            return

        curr = self.head
        for i in range(index):
            curr = curr.next

        newNode = Node(val, curr.next)
        newNode.next = curr.next
        curr.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:  # Invalid index
            return

        prev = self.head
        for i in range(index):
            prev = prev.next

        prev.next = prev.next.next
        self.size -= 1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
