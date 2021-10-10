# Learning about tuples

t = tuple()     # create an empty tuple
print(type(t))

t = ('a',)      # create a tuple with 1 element
print("this is tuple t : ",t)

print('type is ', type(t))

tpl = ('a','b','c')
# tpl('a','b','c')
print(tuple('sequence'))

x,y,z = tpl     #multiple assignment

print(x)
print(y)
print(z)

print('a' in tpl)
print('z' in tpl)