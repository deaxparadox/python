# a = 5

# '''__add__ for the same operation as + operator'''
# print(a.__add__(1))
# print(a.__add__(4))

'''In following example, a class named distance is defined with two instance attributes
- ft and inch. The addition of these two distance objects is desired tobe performed using the
overloading + operator'''

'''To achieve this, the magic method '__add__()' is overridden, which performs the addition
of the ft and inch attributes of the two objects. The '__str__()' method returns the 
object's string representation'''

class distance:
    def __init__(self, x=None, y=None) -> None:
        self.ft = x
        self.inch = y
    def __add__(self, x):
        temp=distance()
        temp.ft=self.ft+x.ft
        temp.inch=self.inch+x.inch
        if temp.inch>=12:
            temp.ft+=1
            temp.inch-=12
            return temp 
    def __str__(self):
        return 'ft:'+str(self.ft)+' in: '+str(self.inch)