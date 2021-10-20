'''
    key -> value store
    any types -> any type
'''

english = {
    'apple': 'fruit blah blah',
    'apetite': 'desire for something, usually food',
    'pluto': 'a gray planet'
}

print(english['apple'])

#print(english['banana']) fails with KeyError

print(english.get('banana')) #handles KeyError and return None

print(english.get('banana', 'unknown word')) #default if not found

english['banana'] = 'yellow fleshy fruit' #add value
print(english.get('banana'))

english['apetizer'] = 'something to create an apetite, usually of food'

print(english.get('apetizer'))

english['pluto'] = 'dwarf gray planet'

print(english.get('pluto'))


