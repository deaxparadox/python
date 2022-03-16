from collections import ChainMap


"""update behind"""
def update_behind():
    a = {'a': 'A', 'c': 'C'}
    b = {'b': 'B', 'c': 'D'}

    m = ChainMap(a,b)
    print("Before: {}".format(m['c']))
    a['c'] = 'E'
    print("After: {}".format(m['c']))
    
def directly():
    a = {'a': 'A', 'c': 'C'}
    b = {'b': 'B', 'c': 'D'}
    m = ChainMap(a,b)
    print('Before:', m)
    m['c']='E'
    print('After: ',m)
    print('a:',a)

def new_child():
    a = {'a': 'A', 'c':'C'}
    b = {'b': 'B', 'c': 'D'}
    
    m1 = ChainMap(a,b)
    m2 = m1.new_child()
    
    print("m1 before: ",m1)
    print("m2 before: ",m2)
    
    m2['c'] = 'E'
    
    print('m1 after: ', m1)
    print('m2 after: ', m2)


def new_child_explicit():
    a = {'a': 'A', 'c':'C'}
    b = {'b': 'B', 'c': 'D'}
    c = {'c': 'E'}
    
    m1 = ChainMap(a,b)
    m2 = m1.new_child(c)
    
    print('m1["c"] = {}'.format(m1['c']))
    print('m2["c"] = {}'.format(m2['c']))
    
new_child_explicit()