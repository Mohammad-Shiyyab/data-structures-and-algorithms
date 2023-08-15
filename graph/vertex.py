from typing import  TypeVar

T = TypeVar('T')


class Vertex():
    def __init__(self, value) :
        self.value = value

    def __str__(self) :
        return str(self.value)
    
    def __repr__(self) :
        return str(self.value)