
line = ' d s a sd d d sd a s d f f f f f d  j k l n mv c x m m l'
count = dict()

words = line.split()
for word in words:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1
print(count)