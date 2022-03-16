"""Capturing Class Attribute definitionorder

PROBLEM
You want to automatically record the order in which attributes and methods 
are defined inside a class body so that you can use it in various operations (e.g,,
serializing, mapping to databases, etc)

SOLUTION
Capturing information about hte body of class definition is easily accomlished thorugh
thatuse of metaclass. Here is an example of a metaclass that uses an OrderedDict
to capture definition order of descriptors
"""

# from collections import OrderedDict

# # A set of descriptors for various types
# class Typed:
#     _expected_type = type(None)
#     def __init__(self, name=None):
#         self._name = name 
        
#     def __set__(self, instance, value):
#         if not isinstance(value, self._expected_type):
#             raise TypeError('Expected ' + str(self._expected_type))
#         instance.__dict__[self._name] = value 
        
# class Integer(Typed):
#     _expected_type = int 

# class Float(Typed):
#     _expected_type = float 

# class String(Typed):
#     _expected_type = str
    
    
# # Metaclass that uses an OrdereDict for class body 
# class OrderedMeta(type):
#     def __new__(cls, clsname, bases, clsdict):
#         d = dict(clsdict)
#         order = [] 
#         for name, value in clsdict.items():
#             if isinstance(value, Typed):
#                 value._name = name 
#                 order.append(name)
#         d['_order'] = order 
#         return type.__new__(cls, clsname, bases, d)
    
#     @classmethod
#     def __prepare__(cls, clsname, bases):
#         return OrderedDict()
    
'''In this metaclass, the definition order of descriptors is captured by using an OrderedDict during
the execution of the class body'''

'''For example, here is a  simole class that uses the ordering to implement a method for
serializing the intance data as  a line of CSV data:'''

# class Structure(metaclass=OrderedMeta):
#     def as_csv(self):
#         return ','.join(str(getattr(self,name)) for name in self._order)
    
# # Example use 
# class Stock(Structure):
#     name = String()
#     shares = Integer()
#     price = Float()
#     def __init__(self, name, shares, price):
#         self.name = name 
#         self.shares = shares
#         self.price = price


from collections import OrderedDict

class NoDupOrderedDict(OrderedDict):
    def __init__(self, clsname):
        self.clsname = clsname 
        super().__init__()
    def __setitem__(self, name, value):
        if name in self:
            raise TypeError('{} already defined in {}'.format(name, self.clsname))
        super().__setitem__(name,value)
        
class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        d['_order'] = [name for name in clsdict if name[0] != '_']
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(cls, clsname, bases):
        return NoDupOrderedDict(clsname)
        