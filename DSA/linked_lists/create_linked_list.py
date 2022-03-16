"""A linked list is a sequence of data elements, which are connected together via links.
Each data elements contains a connection to another data elements in form of a pointer.
We implement the linked lists using the concept of nodes."""

"""CREATION OF LINKED LIST
- created by using the node class
- and create another class use this node class object """

class Node:
    def __init__(self, dataval=None) -> None:
        self.dataval = dataval
        self.nextval = None 
        
class SLinkedList:
    def __init__(self) -> None:
        self.headval = None 
        
list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

#Link first Node to second node 
list1.headval.nextval = e2

# Link second Node to third node 
e2.nextval = e3

