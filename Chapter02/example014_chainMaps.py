
"""
ChainMap Objects
pg. 62-63
"""
from collections import ChainMap

defaults = {
    'theme'     : 'Default',
    'language'  : 'eng',
    'showIndex' : True,
    'showFooter': True
}

# Create a chainMap with defaults
cm = ChainMap(defaults)

print(f'cm.maps ==>> {cm.maps}')
print(f'cm.values() ==>> {cm.values()}')

# Create a new chainMap with a child that overrides the parent
cm2 = cm.new_child({'theme':'bluesky'})
# returns the overriden theme with bluesky
print(f'cm2["theme"] ==>> {cm2["theme"]}')

# Remove the child theme value
cm2.pop('theme')

# see how the default value from the parent is now called
print(f'cm2["theme"] ==>> {cm2["theme"]}')

print(f'cm2.maps ==>> {cm2.maps}')
print(f'cm2.values() ==>> {cm2.values()}')

