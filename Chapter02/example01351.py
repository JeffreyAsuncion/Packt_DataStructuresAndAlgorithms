s1 = {'ab',3,4,(5,6)}
s2 = {'ab',7,(7,6)}

fs1 = frozenset(s1)
fs2 = frozenset(s2)

dict = {fs1:'fs1',fs2:'fs2'}
print(dict)