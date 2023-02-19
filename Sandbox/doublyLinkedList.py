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

    def reverse_iter(self):
        # from tail to head
        current = self.tail
        while current:
            val = current.data
            current = current.prev
            yield val

    def delete(self, data):
        # start at the head
        current = self.head
        # set a node_deleted flag
        node_deleted = False
        # if list is empty - edge case
        if current is None:
            node_deleted = False
        # if data @ head - edge case
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        # if data @ tail - edge case
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        # need to iter to find 
        else:
            # tranverse from head to tail
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_delete = True
                current = current.next
        
        if node_deleted:
            self.count -= 1

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False

    def print_forward(self):
        for node in self.iter():
            print(node)

    def print_backward(self):
        for node in self.reverse_iter():
            print(node)






dd = DoublyLinkedList()

for i in range(101):
    dd.append(i)

print(dd.count)
dd.delete(59)
# print(*dd.iter())
# print(*dd.reverse_iter())
dd.print_backward()