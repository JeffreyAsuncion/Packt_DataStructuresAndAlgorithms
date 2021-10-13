# Dictionaries cont

print(dict(zip('packt', range(5))))

a = dict(zip('packt', range(5)))
print(len(a))

print(a['c'])   # to check the value of a key

print(a.pop('a'))

print(a)

b = a.copy()    # make a copy of the dictionary

print(b)

print(a.keys())

print(a.values())

print(a.items())

a.update({'a':1})   # add an item in the dictionary
print(a)

a.update(a=22)  # update the value of key 'a'

print(a)