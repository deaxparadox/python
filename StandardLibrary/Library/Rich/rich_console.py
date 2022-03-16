from typing import Union
from rich.console import Console

console = Console()

def merge_dict(dict_one, dict_two):
    # merged_dict = Union[dict_one, dict_two]
    merged_dict = {**dict_one, **dict_two}
    console.log(merged_dict, log_locals=True)
    
dict_one = {'id': 1}
dict_two = {'name':'Ashutosh'}
merge_dict(dict_one, dict_two)