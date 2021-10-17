# Sorting dictionaries

d = {'one' : 1, 
     'two' : 2, 
     'three' : 3, 
     'four' : 4,
     'five' :  5,
     'six' : 6}

print(sorted(list(d)))

print(sorted(d.values()))

print(sorted(list(d), key=d.__getitem__))

list_comprehension = [value for (key,value) in sorted(d.items())]
print(list_comprehension)

print(sorted(list(d), key=d.__getitem__, reverse=True))

d2 = {
          'one':'isa',
          'two':'dalawa',
          'three':'tatlo',
          'four':'apat',
          'five':'lima',
          'six':'six'
}
print('d2')
print(sorted(d2, key=d.__getitem__))

print('d2 list comprehension')

list_comprehension_d2 = [d2[i] for i in sorted(d2, key=d.__getitem__)]
print(list_comprehension_d2)

def corder(string):
     return (string[len(string)-1])


print('sort by last letter')
print(sorted(d2.values(), key=corder))



















