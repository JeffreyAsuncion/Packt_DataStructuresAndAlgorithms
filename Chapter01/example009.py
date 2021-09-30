# Functions as first-class objects

def greeting(language):
    if language=='eng':
        return 'hello world'
    if language=='fr':
        return 'Bonjour le monde'
    else:
        return 'language not supported!'

l = [greeting('eng'),greeting('fr'),greeting('ger')]
print(l[1])

def callf(f):
    lang='eng'
    return (f(lang))

print(callf(greeting))