'''__new__() magic method is implicity called before the __init__() method.
The __new__() method returns a new object, which is then initialized by __init__()'''

class Employee:
    def __new__(cls):
        print("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst
    
    def __init__(self) -> None:
        print("__ini__ magic method is called")
        self.name = "Satya"