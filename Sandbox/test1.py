class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val


    def delete(self, data):
        current = self.tail
        prev = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.count -= 1
                return

            prev = current
            current = current.next



s1 = SinglyLinkedList()

for i in range(0,100,2):
    s1.append(i)

print(list(s1.iter()))
s1.delete(50)
print(list(s1.iter()))
