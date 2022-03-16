import collections 

def func1():
    print(collections.Counter(['a','b','c','a','b','b']))
    print(collections.Counter({'a':2, 'b':3, 'c':1}))
    print(collections.Counter(a=2, b=3, c=1))
    
def func2():
    c = collections.Counter()
    print("Initial :", c)
    
    c.update('abcdaab')
    print("Sequence: ", c)
    c.update({'a':1, 'd': 5})
    print("Dict     :",c)    
    
func2()