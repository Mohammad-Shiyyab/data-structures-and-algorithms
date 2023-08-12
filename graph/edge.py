from typing import TypeVar
from .vertex import Vertex


T = TypeVar('T')


class Edge():
    def __init__(self, vertex, weight = None) :
        self.vertex = vertex
        self.weight = weight

    def __str__(self) :
        return str(self.vertex) + ' : ' + str(self.weight)

    def __repr__(self) :
        return str(self.vertex)