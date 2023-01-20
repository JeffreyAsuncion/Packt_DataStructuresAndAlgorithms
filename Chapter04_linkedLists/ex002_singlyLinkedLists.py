
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
            # point self.head.next ==>> new node
            self.head.next = node
            # reset  self.head ==>> new node
            self.head = node
            print('adding')
        else:
            # note the tail is stationary, while the head grows
            # since list is empty
            # point tail and head ==>> new node 
            # tail is stationary
            self.tail = node
            # new nodes are appended to head
            self.head = node
            print('1st add')
        self.count += 1
    
    # this creates a "list" of data
    # actually a generator to be used below
    # https://realpython.com/introduction-to-python-generators/
    def iter(self):
        """ Iterate through the list. """
        # a generator of data values
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
            # if you found the data point
            if current.data == data:
                # if you are at endpoint tail
                if current == self.tail:
                    # point tail to current.next
                    # don't lose the tail
                    self.tail = current.next
                else:
                    # not at tail endpoint
                    # delete current by skipping current 
                    # point prev.next to current.next
                    prev.next = current.next
                self.count -= 1
                return
            # iterate prev and current
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
        # index is out of range
        if index > self.count - 1:
            raise Exception("Index out of range.")
        # start at the tail endpoint
        current = self.tail
        # iterate up to but not including index
        for n in range(index):
            current = current.next
        # drops off at the index
        return current.data

    # this allows s[i] = newData to __setitem__
    def __setitem__(self, index, value):
        # index is out of range
        if index > self.count - 1:
            raise Exception("Index out of range.")
        # start at the tail endpoint
        current = self.tail
        # iterate up to but not including index
        for n in range(index):
            current = current.next
        # replace old value with new value
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