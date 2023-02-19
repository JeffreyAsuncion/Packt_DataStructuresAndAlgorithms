# this is a stack implementation created with Nodes


# the node is the underlying structure
# the user should not have access to the Node class
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
        # if there is a node at top
        if self.top:
            # point self.top to  new node.next 
            node.next = self.top
            # point top to new node
            self.top = node
        # otherwise no node at top
        else:
            # no top, point top to new node
            self.top = node
        # increment size 
        self.size += 1

    def peek(self):
        if self.top:
            return self.top.data
        return None

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                # set top to top.next
                self.top = self.top.next
            # otherwise no top
            else:
                return None

s1 = Stack()
s1.push(10)
print(s1.peek())
s1.push(11)
print(s1.peek())
s1.push(12)
print(s1.peek())
s1.pop()
print(s1.peek())
