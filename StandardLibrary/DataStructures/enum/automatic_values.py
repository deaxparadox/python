from enum import Enum, auto 
class Color(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    
print(list(Color))


# 
class AutoName(Enum):
    def _generate_next_value(name, start, count, last_values):
        return name 
    
class Ordinal(AutoName):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()
    
print(list(Ordinal))