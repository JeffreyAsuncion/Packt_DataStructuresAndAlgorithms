from collections import defaultdict

def isPrimaryColor(c):
    if (c=='red') or (c=='blue') or (c=='yellow'):
        return True
    return False



dd = defaultdict(int)

words = str.split('red blue green red yellow blue red green green red')

for word in words:
    if isPrimaryColor(word):
        dd[word] += 1
    
print(dd)