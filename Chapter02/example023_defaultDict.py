from collections import defaultdict

dd = defaultdict(int)
words = str.split(' red blue green red yellow blue red green green red')
for word in words: dd[word] += 1

print(dd)


def isprimary(c):
    if (c=='red') or (c == 'blue') or (c == 'green'):
        return True
    else:
        return False
