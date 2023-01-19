
"""
https://github.com/PacktPublishing/Hands-On-Data-Structures-and-Algorithms-with-Python-Second-Edition/blob/master/Chapter04/singly_linked_list.py
"""

class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """ A singly-linked list. """
    def __init__(self):
        """ Create an empty list. """
        self.tail = None
        self.head = None
        self.count = 0

    def append(self, data):
        """ Append an item to the list """
        node = Node(data)
        if self.head:
            # note the tail is stationary, while the head grows
            self.head.next = node
            self.head = node
            print('adding')
        else:
            # note the tail is stationary, while the head grows
            self.tail = node
            self.head = node
            print('1st add')
        self.count += 1
    
    # this creates a "list" of data
    # actually a generator to be used below
    # https://realpython.com/introduction-to-python-generators/
    def iter(self):
        """ Iterate through the list. """
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    

    def delete(self, data):
        """ Delete a node from the list """
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

    def search(self, data):
        """ Search through the list. Return True if data is found, otherwise
        False. """
        for node in self.iter():
            if data == node:
                return True
        return False

    # this allows s[i] to __getitem__
    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.tail
        for n in range(index):
            current = current.next
        return current.data

    # this allows s[i] = newData to __setitem__
    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.tail
        for n in range(index):
            current = current.next
        current.data = value


# sll = SinglyLinkedList()
# for i in range(100,120):
#     sll.append(i)

# print(sll.search(100))

# print(sll.__getitem__(10))

##################################

words = SinglyLinkedList()
words.append('foo')
words.append('bar')
words.append('bim')
words.append('baz')
words.append('quux')

print("access by index")
print("here is a node: {}".format(words[1]))

print("modify by index")
words[4] = "Quux"
print("Modified node by index: {}".format(words[4]))

# print("This list has {} elements.".format(words.count))
# for word in words.iter():
#     print("Got this data: {}".format(word))

# if words.search('foo'):
#     print("Found foo in the list.")
# if words.search('amiga'):
#     print("Found amiga in the list.")

# print("Now we try to delete an item")
# words.delete('bim')
# print("List now has {} elements".format(words.count))
# for word in words.iter():
#     print("data: {}".format(word))

# print("delete the first item in the list")
# words.delete('foo')
# print("size: {}".format(words.count))
# for word in words.iter():
#     print("data: {}".format(word))

# print("delete the last item in the list")
# words.delete('quux')
# print("size: {}".format(words.count))
# for word in words.iter():
#     print("data: {}".format(word))