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