from datetime import date 
class Person:
    def __init__(self,name,age) -> None:
        self.name = name 
        self.age = age

    # a class method to create a 
    # person object by birth year 
    @classmethod 
    def fromBirthYear(cls,name,year):
        return cls(name,date.today().year -year)
    
    def display(self):
        print("Name: ",self.name, "Age: ",self.age)

person = Person("mayank",21)
person.display()

