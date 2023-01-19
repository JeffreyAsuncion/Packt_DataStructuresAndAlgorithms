class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            # point self.head.next ==>> new node
            self.head.next = node
            # reset  self.head ==>> new node
            self.head = node
        # self.head == None, list is empty
        else:
            # since list is empty
            # point tail and head ==>> new node 
            # tail is stationary
            self.tail = node
            # new nodes are appended to head
            self.head = node
        self.size += 1

    def  



s = SinglyLinkedList()

for i in range(100):
    s.append(i)

print(s.size)

