"""QUEUE
- the items are allowed at on end but removed from the other end. So it is FIFO (First In First Out)

- A queue can be implemented using python list where we use the 'insert()' and 'pop()'
methods to add and remove elements. Their is no insertion as data elements are always 
added at the end of the queue."""


class Queue(object):
    def __init__(self) -> None:
        self.queue = list()
        
    """Adding Elements"""
    # Insert method to add element 
    def addtoq(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True 
        else:
            return False 
    
    def size(self):
        return len(self.queue)
    
    """Removing an element"""
    # pop method to remove element
    def removefromq(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return "No elements in Queue!"
    