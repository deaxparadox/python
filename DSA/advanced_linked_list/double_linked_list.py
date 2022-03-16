"""DOUBLE LINKED LIST
- coutains a links element called first and last.
- each link carries a data fiels(s) and two link fields called next and prev 
- each link is linked with its next link using its next link 
- each  link is linked with its previous link using its previous link 
- the last link crries a link as null to mark the end of the link."""


class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None 
        self.prev = None 
        
class doubly_linked_list:
    def __init__(self) -> None:
        self.head = None 
        
    # Adding data element 
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
        
    # Print the Double linked list 
    def listprint(self, node):
        while node is not None:
            print(node.data, end=" ")
            last = node 
            node = node.next 
            
    # insert method to insert the element 
    def insert(self, prev_node, NewVal):
        if prev_node is None:
            return 
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode
            
def main():
    dllist = doubly_linked_list()
    dllist.push(12)
    dllist.push(8)
    dllist.push(62)
    dllist.insert(dllist.head.next, 13)
    dllist.listprint(dllist.head)
    
if __name__ == "__main__":
    main()
    print()