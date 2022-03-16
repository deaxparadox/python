class Portal:
    
    def __init__(self) -> None:
        self.__name = ''
    
    # using @property decorator
    @property
    # Getter method 
    def name(self):
        self.__name
    
    # Setter method 
    @name.setter
    def name(self, val):
        self.__name = val
    
    # Deleter method 
    @name.deleter 
    def name(self):
        del self.__name 
        
        
def run():
    # Creating object 
    p = Portal();
    # Setting name 
    p.name = "Everything"
    # Prints name 
    print(p.name)
    # Deletes name 
    del p.name
    
    # As name is deleted above this 
    # will throw an error 
    # print(p.name)
    
if __name__ == "__main__":
    run()