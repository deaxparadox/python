"""
- This involves changing the pointer to a specific node to point 
to the new node. That is possible by passing in both the new node 
and the existing node after which the new node will be inserted. So 
we define an additional class which will change the next pointer of the new
node to the next pointer of middle node. then assign tthe new node to 
next pointer of the middle node.
"""

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval 
        self.nextval = None 
        
class SLinkedList:
    def __init__(self):
        self.headval = None 
        
    # function to add node 
    def Inbetween(self, middle_node , newdata):
        if middle_node is None:
            print("This mentioned node is absent")
            return 

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval 
        middle_node.nextval = NewNode
        
    # print the linked list 
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

list.headval.nextval = e2
e2.nextval = e3

list.Inbetween(list.headval.nextval,"Fri")

list.listprint()