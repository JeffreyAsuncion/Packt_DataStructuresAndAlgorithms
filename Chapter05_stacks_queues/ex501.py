class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def push(self, data):
        node = Node(data)
        # if top is occupied
        if self.top:
            # add newNode node
            node.next = self.top
            # newNode node become new top of stack
            self.top = node
        # if top is not occupied
        else:
            # newNode node become new top of stack
            self.top = node
        self.size += 1
        
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None
        
    def peek(self):
        if self.top:
            return self.top.data
        return None
    