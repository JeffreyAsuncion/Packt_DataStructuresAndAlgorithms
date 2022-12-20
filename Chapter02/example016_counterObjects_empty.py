from collections import Counter

# Create an empty counter object
ct = Counter()

# print(ct)

# Populate the object with .update
ct.update('abca')

# print(ct)

# update the count fo 'a' by adding addition counts
ct.update({'a':3})

print(ct)

for item in ct:
    print('%s: %d' % (item, ct[item]))
    
    
print("\nusing elements()")

print(f'ct["x"] ==>> {ct["x"]}')

print(sorted(ct.elements()))

# most_common() method
print(ct.most_common())

# subtract() method
ct.subtract({'a':3})
print(ct)