"""STACK
- the element inserted last in sequence will come out first as we can 
remove only from the top of the stack. Such feature is know is Last In Fast Out
(LIFO) featuer.
The operations of adding and removing the elements is known as PUSH and 
POP. 

- the following example we implement it as 'add' and 'remove' functions."""


class Stack:
    def __init__(self) -> None:
        self.stack = []

    """PUSH INTO A STACK"""
    # use list to append method to add element
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True 
        else:
            return False 
    
    # Use peek to loop at the top of the stack 
    def peek(self):
        return self.stack[-1]
    
    """POP FROM A STACK"""
    # Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return "No element in the Stack"
        else:
            return self.stack.pop()
