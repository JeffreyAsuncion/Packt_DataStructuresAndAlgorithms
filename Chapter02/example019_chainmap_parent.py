from collections import ChainMap

default = {
    'theme'     : 'Default',
    'language'  : 'eng',
    'showIndex' : True
}

cm = ChainMap(default) # creates a chainMap with defaults configuration
print(cm)
print()
print(cm.maps)
print()
print(cm.values())
print(cm['theme'])
print()
print("create a new chainmap with a child that overides the parent")

cm2 = cm.new_child({'theme':'bluesky'})
print(cm2['theme'])
print('pop')
cm2.pop('theme')
print(cm2['theme'])
print()
print(cm2.maps)
print(cm2.parents)

