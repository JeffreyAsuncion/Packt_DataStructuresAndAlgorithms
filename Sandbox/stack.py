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
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
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
                self.top = self.top.next
                return data
            else:
                return None
                

    def _show_all(self):
        current = self.top
        while current:
            print(f" {current.data} ===>>> ")
            current = current.next

    


s1 = Stack()
# s1.push(100)
# s1.push(10)
# s1.push(40)
# s1.push(50)
# s1._show_all()
# print(s1.pop())
# # print(s1.peek())
for i in range(1,100):
    s1.push(i)
s1._show_all()