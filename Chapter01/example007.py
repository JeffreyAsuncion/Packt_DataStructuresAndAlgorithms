# string examples

greet = 'hello world'

print(greet[1])
print(greet[0:8])
print(greet[0:8:2])
print(greet[0::2])
print(greet[1+2])
print(greet[len(greet)-1])

for i in enumerate(greet[0:5]):
    print(i)

print(greet[:5] + ' wonderful ' + greet[5:])

x='3'; y='2'
print(x+y)
print(int(x)+ int(y))