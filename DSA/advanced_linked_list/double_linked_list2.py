class _DoubleLinkedBase:
    """A base class providing a doubly linked representation"""
    
    class _Node:
        """Lightweight, nonpublic class for sorting a doubly linked node"""
        __slots__ == "_element", "_prev", "_next"       # streamline memory
        
        def __init__(self, element, prev, next):        # initialize node's fields
            self._element = element             # user's element 
            self._prev = prev                       # preivous node reference
            self._next = next                       # next node reference 
    
    
    def __init__(self) -> None:
        """Create an emtpy list"""    
        self._header = self._Node(None, None, None)
        self._trailor = self._Node(None, None, None)
        self._header._next = self._trailor              # trailer is after header   
        self._trailor._prev = self._header              # header is before trailor
        self._size = 0                                               # number of elements
        
    def __len__(self):
        """Return the number of elements in the list."""
        return self._size
    
    def is_empty(self):
        """Return True if list is emtpy"""
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)      # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element"""
        predecessor = node._prev
        successor = node._next 
        predecessor._next = successor
        successor._prev = predecessor
        self._size -=1
        element = node._element                     # record deleted element 
        node._prev = node._next = node._element = None          # deprecate node 
        return element                                                                   # return deleted element 
    

class LinkedDeque(_DoubleLinkedBase):           # note the user of inheritence 
    """Double-ended queue implementation based on double linked list """
    
    def first(self):
        """Return (but do not remove) the element at the front of the deque"""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element          # real item just after header 
    
    def last(self):
        """Return (but do not remove) the element at the back of the deque"""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailor._prev._element             # real item just before trailer  
    
    def insert_first(self, e):
        """Add an element to the fron of the dequee"""
        self._insert_between(e, self._header, self._header._next)       # after header 
    
    def insert_last(self, e):
        """Add an element tothe back of the deque"""
        self._insert_between(e, self._trailor._prev, self._trailor)         # before trailor
        
    def delete_first(self):
        """Remove and return the element from the front of the deque
        
        Raise Empty exception if the deque is empty"""
        
        if self.is_empty():
            raise Emtpy("Deque is empty")
        return self._delete_node(self._header._next)            # use inherited method 
    
    def delete_list(self):
        """Remove and return the element from the back of the deque
        
        Raise Empty exception if the deque is emtpy
        """
        if self.is_empty():
            raise Empty("Deque is emtpy")
        return self._delete_node(self._trailor._prev)                   # use inherited method 