from typing import List, Tuple, Dict, Union
# n : int = 8

# name : str = "Deepanshu"

def sum(a: int, b: int) -> int:
        return a+b 
print(sum(3,5))

# List of Integer
numbers: List[int] = [1,2,3,4,5]

#Type of a string and an Integer.
person: Tuple[str, int] = ("Deepanshu", 18)

# Dictionary with string keys and Integer values
scores: Dict[str, int] = {"Deepanshu":100, "Harvey": 101}

# Union type of variables that can hold multiple types
identifier: Union[int, str] = "ID888"