"""Single linked lists can be traversed in only forward direction starting 
from the first data element

We simply print the value of the next data element by assigning the 
pointer of the next node to the current data element."""

class Node:
    def __init__(self, dataval = None) -> None:
        self.dataval = dataval 
        self.nextval = None 
        
class SLinkedList:
    def __init__(self) -> None:
        self.headval = None 
    
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            
            
List = SLinkedList()
List.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

#Link first Node to second node 
List.headval.nextval = e2

# Link second Node to third node 
e2.nextval = e3

List.listprint()
