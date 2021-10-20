# Sets

s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
print(s1)

s1.remove(4)
print(s1)

s1.discard(3)
print(s1)

s1.clear()
print(s1)

print("="*20)

s1 = {'ab',3,4,(5,6)}
s2 = {'ab',7,(7,6)}

print("same as s1.difference(s2)")
print(s1-s2)

print("s1.intersection(s2)")
print(s1.intersection(s2))

print("s1.union(s2)")
print(s1.union(s2))

print('ab' in s1)
print('ab' not in s1)

for element in s1:
    print(element)