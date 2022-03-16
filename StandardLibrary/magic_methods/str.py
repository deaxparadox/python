'''It is overridden to return a printable string representation of any user defined class.
We have seen 'str()' build-in function which returns a string from the object parameter.'''

'''for ex. str(12) returns '12'. When invoked, it calls the '__str__()' method in the int class'''

# let us now override the __str__() method inthe Employee class to return a 
# string representation of its object.

class Employee:
    def __init__(self) -> None:
        self.name = "Nitish"
        self.salary = 10000
    def __str__(self):
        return 'name='+self.name+' salary=$'+str(self.salary)
    
'''See how the str() function internally calls the __str__() method defined in the Employee class.
This is why it is called a magic method! '''