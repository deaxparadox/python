from pydantic import BaseModel

class Person(BaseModel):
    name: str 
    age: int 
    class Config:
        schema_extra = {
            'examples': [
                {
                    'name': 'John Doe',
                    'age': 25,
                }
            ]
        }
        
# print(Person.schema_json(indent=2))

from typing import Dict, Any, Type 
class Person(BaseModel):
    name: str 
    age: int 
    class Config:
        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type['Person']) -> None:
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)
                
print(Person.schema_json(indent=2))