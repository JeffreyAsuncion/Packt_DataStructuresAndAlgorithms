"""
https://github.com/PacktPublishing/Hands-On-Data-Structures-and-Algorithms-with-Python-Second-Edition/blob/master/Chapter05

"""

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

def check_brackets(statement):
    stack = Stack()

    for ch in statement:
        if ch in ('{','[','('):
            stack.push(ch)
        if ch in ('}',']',')'):
            last = stack.pop()
            if (last == '{') and (ch == '}'):
                continue
            elif (last == '[') and (ch == ']'):
                continue
            elif (last == '(') and (ch == ')'):
                continue
            else:
                return False
    
    if stack.size > 0:
        return False
    else:
        return True


s1 = {
    "{(foo)(bar)}[hello](((this)is)a)test",
    "{(foo)(bar)}[hello](((this)is)atest",
    "{(foo)(bar)}[hello](((this)is)a)test))"
}

for s in s1:
    m = check_brackets(s)
    print("{}: {}".format(s, m))