"""In general nodes are known are pointer as in c. But in python it's called Nodes.

Nodes are foundations on which variout data strucures linked listes and trees can 
be handled in python"""

"""CREATION OF NODES 
The nodes are created by implementing a class which hold the pointers along with  the data 
element."""

# class daynames:
#     def __init__(self, dataval=None):
#         self.dataval = dataval      # 
#         self.nextval = None     # 
        
# e1 = daynames('Mon')
# e2 = daynames("Tue")
# e3 = daynames('Wed')

# e1.nextval = e3
# e3.nextval = e2


"""TRAVERSING THE NODE ELEMENTS
"""
class daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval      # 
        self.nextval = None     # 
        
e1 = daynames('Mon')
e2 = daynames("Tue")
e3 = daynames('Wed')
e4 = daynames('Thu')
e5  = daynames('Fri')

e1.nextval = e3
e3.nextval = e2
e2.nextval = e4

# for loop 
# e4.nextval = e1

thisvalue = e1

while thisvalue:
    print(thisvalue.dataval)
    thisvalue = thisvalue.nextval

