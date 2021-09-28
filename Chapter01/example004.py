# Flow control and iteration

x = 0
while x < 3:
    print(x); x += 1

x = 'one'
if x == 0:
    print('False')
elif x == 1:
    print('True')
else:
    print('Something else')

words = ['cat', 'dog', 'elephant']
for w in words:
    print(w)