class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        self.items.insert(0, data)      # Always insert items at index 0
        self.size += 1                  # increment the size of the queue by 1
    
    def dequeue(self):
        data = self.items.pop()         # delete the topmost item from the queue
        self.size -= 1                  # decrement the size of the queue by 1
        return data



lq = ListQueue()
lq.enqueue(1)
lq.enqueue(2)
lq.enqueue(3)
print(lq.items)