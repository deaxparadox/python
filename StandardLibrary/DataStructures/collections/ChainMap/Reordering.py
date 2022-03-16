from collections import ChainMap

"""collections chain map recorder"""
a = {'a':'A', 'c':'C'}
b = {'b':'B', 'c':'D'}

m = ChainMap(a,b)

print(m.maps)
print('c = {}\n'.format(m['c']))

# Reverse the list 
m.maps = list(reversed(m.maps))

print(m.maps)
print('c = {}'.format(m['c']))