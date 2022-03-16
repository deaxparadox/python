# class C:
#     def __init__(self) -> None:
#         self._x = None 
#     @property
#     def x(self):
#         return self._x 
#     @x.setter
#     def x(self,value):
#         self._x=value 
#     @x.deleter
#     def x(self):
#         del self._x


class PT:
    def __init__(self) -> None:
        self.__current = None 
    
    @property
    def current(self):
        return self.__current
    @current.setter
    def current(self,value):
        self.__current = value 
    @current.deleter
    def current(self):
        del self.__current
        
if __name__ == "__main__":
    pt = PT()
    print(pt.current)
    pt.current = "AI"
    print(pt.current)
    del pt.current
    try:
        print(pt.current)
    except: 
        pt.current = None
        print(pt.current)
    pt.current = "Electricity"
    print(pt.current)
    del pt.current 
    # print(pt.current)
    pt.current = None 