"""We can remove an existing node using the key for that node. 
- we locate the previous node of the node which is to be deleted. 
Then, point the next pointer of this node to the next node to be deleted"""

class Node:
    def __init__(self, data=None):
        self.data = data 
        self.next = None 
        
class SLinkedList:
    def __init__(self):
        self.head = None 
        
    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head 
        self.head = NewNode
        
    # function to remove node 
    def RemoveNode(self, RemoveKey):
        HeadVal = self.head 
        
        if (HeadVal is not None):
            if HeadVal.data == RemoveKey:
                self.head = HeadVal.next 
                HeadVal = None 
                return 
        
        while HeadVal is not None:
            if HeadVal.data == RemoveKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        
        if HeadVal == None:
            return 
        
        prev.next = HeadVal.next
        HeadVal = None
        
    def LListprint(self):
        printval = self.head 
        while printval:
            print(printval.data)
            printval = printval.next 
            

llist = SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.RemoveNode("Tue")
llist.LListprint()