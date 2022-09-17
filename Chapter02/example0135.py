s1 = {'ab',3,4,(5,6)}
s2 = {'ab',7,(7,6)}

print("this is the difference",s1-s2) # same as s1.difference(s2)
print("intersection ",s1.intersection(s2))

print("union ",s1.union(s2))

print('ab' in s1, 'ab' not in s1)

for element in s1: print(element)

# print("this will cause an error", s1.add(s2))
s1.add(frozenset(s2))
print("this fixes it", s1)


