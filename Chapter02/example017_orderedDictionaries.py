import collections

od1 = collections.OrderedDict()
od1['one'] = 1
od1['two'] = 2

od2 = collections.OrderedDict()
od2['two'] = 2
od2['one'] = 1

print(od1 == od2)

kvs = [('three',3), ('four',4), ('five',5)]
od1.update(kvs)

print(od1)

for k,v in od1.items():
    print(k,v)
    
od3 = collections.OrderedDict(sorted(od1.items(), key=lambda t : (4*t[1]) - t[1]**2))
print(od3)
print(od3.values())