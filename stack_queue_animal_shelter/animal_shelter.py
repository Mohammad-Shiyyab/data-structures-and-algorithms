from typing import Literal, Union
from stack_queue_animal_shelter.animal import Animal, Cat, Dog


class AnimalShelter:
    
    def __init__(self):
        self.animals: list[Animal] = []

    def enqueue(self, animal: Animal):
        if isinstance(animal, (Dog, Cat)):
            self.animals.append(animal)
            
        else:
            raise TypeError("Animal must be a Dog or Cat")

    def dequeue(self, pref = None ):

        if pref is None and len(self.animals) > 0:
            return self.animals.pop(0)

        for i, animal in enumerate(self.animals):
            if animal.species == pref:
                return self.animals.pop(i)

        return None