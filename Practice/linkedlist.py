class node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def appendLast(self, value):
        new_node = node(value)

        if self.head == None:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            current.next.next = None

    def display(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def reverse(self):
        curr = self.head
        prev = node()
        while curr:
            temp = curr.next
            curr.next = prev
            curr = temp




akku = linkedList()
akku.appendLast(5)
akku.appendLast(6)
akku.appendLast(7)
akku.reverse()
akku.display()
