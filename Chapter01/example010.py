# higher order functions

list = [1,2,3,4,5]

for item in map(lambda n: n*2, list): 
    print(item)


for item in filter(lambda n: n<4, list):
    print(item)

words = str.split('The longest work in this sentence')
print(sorted(words, key=len))


sl = ['A','b','a','C','c']
sl.sort(key=str.lower)
print(sl)
sl.sort()
print(sl)

items = [["rice",2.4,8],["flour", 1.9, 5],["corn", 4.7, 6]]
items.sort(key=lambda item: item[1])
print(items)


print(items[1][1])

l = [2,4,8,16]
print([i**3 for i in l])

