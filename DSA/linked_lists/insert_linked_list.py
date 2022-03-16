"""
- involves reassigning the pointers from the existing nodes to the newly
inserted node. Depending on whether the new data element is getting 
inserted at the begining or at the middle or at the end of the linked list 
"""

"""INSERTING AT THE BEGINING 
- this involvse pointing the next pointer of the new data to the current head of 
the linked list.
- So the current head of the linked list becomes the second data element 
and the new node becomes the head of the linked list."""

class Node:
    def __init__(self, dataval=None) -> None:
        self.dataval =dataval
        self.nextval = None
        
class SLinkedList:
    def __init__(self) -> None:
        self.headval = None 
        
    # Print the linked list 
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval 
    
    
    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        
        # Update the new nodes next to val to existing node 
        NewNode.nextval = self.headval
        self.headval = NewNode

def insert_at_begining():
 
    List = SLinkedList()
    List.headval = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")

    List.headval.nextval = e2
    e2.nextval = e3       
            
    # inserting at begining         
    List.AtBegining("Sun")
    List.listprint()


    e4 = Node("Thu")    # forth node 
    e3.nextval = e4         # linked forth to thrid


"""INSERTING AT THE END 
- this involves pointing the next pointer of the current last node of the 
linked list to the new data node. So the current last node ofthe linked list 
becomdes the second last data node and the new node becomes the last 
node of the linked list."""

class Node:
    def __init__(self, dataval=None) -> None:
        self.dataval = dataval 
        self.nextval = None 
        
class SLinkedList:
    def __init__(self) -> None:
        self.headval = None 
        
    # Function to add newnode 
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return 
        laste = self.headval
        while (laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode
        
    # Print the linked list 
    def listprint(self):
        printval = self.headval 
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            
def insert_at_end():
    list = SLinkedList()
    list.headval = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")

    list.headval.nextval = e2
    e2.nextval = e3

    list.AtEnd("Thu")

    list.listprint()
    
insert_at_end()