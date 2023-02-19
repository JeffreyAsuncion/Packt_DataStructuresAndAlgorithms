class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList(object):
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
                self.count += 1
                return
            prev = current
            current = current.next
            
    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
            return False

    def __getitem__(self, index):
        if index > self.count - 1 :
            raise Exception("Index out of range")
        current = self.tail
        for n in range(index-1):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range")
        current = self.tail
        for n in range(index-1):
            current = current.next
        current.data = value







if __name__ == '__main__':
    sll = SinglyLinkedList()

    for i in range(20):
        sll.append(i)

    print(sll.count)
    print(*sll.iter())

    print(sll[9])
    sll[10] = 90
    print(*sll.iter())
    sll.delete(90)
    print(*sll.iter())

