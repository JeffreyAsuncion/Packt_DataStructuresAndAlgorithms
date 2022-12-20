from collections import namedtuple

space = namedtuple('space', 'x y z')

# # we can also use the space (2.0, 4.0, 10)
s1 = space(x=2.0, y=4.0, z=10)

print(s1)
print(s1.x * s1.y * s1.z)


# Three methods to try
# _make(), asdict(), _replace

s1 = [4,5,6]
s1 = space._make(s1)
print(s1.x)

print(s1._asdict())

s1._replace(x=7, y=4, z=9)
print(space._fields)
print(space._fields_defaults)