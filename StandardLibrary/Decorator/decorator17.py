'''
class MyMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        # clsname is name of class being defined
        # bases is tuple of bases classes
        # clsdict is class dictionary
        return super().__new__(cls, clsname, bases, clsdict)

# Alernatively if __init__() is defined:
# class MyMeta(type):
#     def __init__(self, clsname, bases, clsdict):
#         super().__init__(clsname, bases, clsdict)
#         # clsname is name of class being defined
#         # bases is typle of base classes 
#         # cls dict is class dictionary
        
        
# To use a metaclass, you would generally incorporate in into a 
# top-level base class from which other objects inherit
class Root(metaclass=MyMeta):
    pass 

class A(Root):
    pass 

class B(Root):
    pass 
'''

class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            # print(name, name.lower())
            if name.lower() != name:
                raise TypeError("Bad attribute name: ", + name)
        return super().__new__(cls, clsname, bases, clsdict)

class Root(metaclass=NoMixedCaseMeta):
    pass 

class A(Root):
    def foo_bar(self): pass     # Ok 
    
class B(Root):
    def fooBar(self): pass      # TypeError