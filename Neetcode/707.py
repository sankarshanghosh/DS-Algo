class MyLinkedList:

    def __init__(self):
        self.stack = []

    def get(self, index: int) -> int:
        if index < len(self.stack):
            return self.stack[index]
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.stack.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.stack.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < len(self.stack):
            self.stack.insert(index, val)
        elif index == len(self.stack):
            self.stack.append(val)

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.stack):
            self.stack.pop(index)
