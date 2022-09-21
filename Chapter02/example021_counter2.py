from collections import Counter

ct = Counter() # creates an empty counter object
print(ct)

ct.update('abca') # populates the object
print(ct)

ct.update({'a':3}) # updates the count of 'a'
print(ct)

for item in ct:
    print('%s: %d' % (item,ct[item]))

print()
print(ct)
print(ct['x'])

ct.update({'a':-3, 'b':-2, 'e':2})
print(ct)

print(sorted(ct.elements()))



