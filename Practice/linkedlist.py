from email import header


class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head

        while cur.next != None:
            cur = cur.next
        cur.next = new_node