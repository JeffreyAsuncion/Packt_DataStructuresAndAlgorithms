class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # adding to the tail
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def iter(self):
        # from head to tail
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    



dd = DoublyLinkedList()

for i in range(101):
    dd.append(i)

print(dd.count)