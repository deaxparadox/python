

class Dequeue:
    def __init__(self) -> None:
        self.__deque = []
        
    """left : insert()"""
    def left(self, dataval):
        if dataval not in self.__deque:
            self.__deque.insert(0, dataval)
            return True 
        else:
            return False 
        
    """right : append()"""
    def right(self, dataval):
        if dataval not in self.__deque:
            self.__deque.append(dataval)
            return True 
        else:
            return False 
    
    """popright : pop()"""
    def popright(self):
        if len(self.__deque) <= 0:
            return "No element in the Stack"
        else:
            return self.__deque.pop()
        
    """popleft: assign and delete first element"""
    def popleft(self):
        if len(self.__deque) <= 0:
            return "No element in the dequeue"
        else:
            fe = self.__deque[0]                  # first element
            rest_arr = self.__deque[1:]       # assiging array from element 1 
            self.__deque = rest_arr            # reassing new array
            return fe
            
    
    # check if len  
    def is_empty(self):
        return len(self.__deque) == 0
    
    # return deque
    def deque(self):
        return self.__deque