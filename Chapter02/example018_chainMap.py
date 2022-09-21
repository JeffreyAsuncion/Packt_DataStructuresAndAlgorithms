# chain map

import collections
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'d':4, 'e':5}
chainmap = collections.ChainMap(dict1, dict2) # linking two dictionaries
print(chainmap)
print()
print(chainmap.values)
print()
print(chainmap['b'])
print()
print(chainmap['e'])