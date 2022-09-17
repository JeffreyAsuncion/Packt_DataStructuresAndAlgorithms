# Deques - pronounced Decks

from collections import deque
import itertools

dq = deque('abc') #creates deque(['a','b','c'])
print(dq)

dq.append('d')  #adds the value 'd'to the right
print(dq)

dq.appendleft('z') # adds the value 'z' to the left
print(dq)

dq.extend('efg')  #adds the value 'efg'to the right
print(dq)

dq.extendleft('yxw') # adds the value 'yxw' to the left
print(dq)




dq.pop()  #pops and removes the value 'g' from the right
print(dq)

dq.popleft() # pops and removes the value 'w' from the left
print(dq)


dq.rotate(2)  #rotates all itmes 2 steps to the right
print(dq)

dq.rotate(-2)  #rotates all itmes 2 steps to the left
print(dq)

a = list(itertools.islice(dq,3,9))
print(a)