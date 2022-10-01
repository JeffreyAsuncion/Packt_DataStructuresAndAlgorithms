from collections import namedtuple

space = namedtuple('space','x y z')
s1 = space(x=2.0, y=4.0, z=10) # we can also use space(2.0,4.0,10)
print(s1)

print(s1.x * s1.y * s1.z) # calculate volume



s1 = [4,5,6]
s1 = space._make(s1)
print(s1[0])


print(s1._asdict())
s1._replace(x=7, z=9)
print(space._fields)
print(space._field_defaults)