from collections import Counter

print(Counter('anysequence'))

# counter with string
c1 = Counter('anysequence')

# counter with dictionary (key:value) pair
c2 = Counter({'a':1, 'c':1, 'e':1})

# counter with set
c3 = Counter(a=1, c=1, e=1)

print('\nc1')
print(c1)
print('\nc2')
print(c2)
print('\nc3')
print(c3)

for i in c1:
    print(i)