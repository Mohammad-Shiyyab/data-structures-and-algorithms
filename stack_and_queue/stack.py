
class Node():
    def __init__(self,value=None):
        
        self.value=value
        self.next=None


class Stack():

    def __init__(self,top=None) :
        self.top = top

    def push(self, value) :
        
        old_top = self.top
        self.top = Node(value)
        self.top.next = old_top
        
    def pop(self):
       
        
        
        if self.top is None:
            raise Exception("Cannot pop from an empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        
        if self.top is None:
            raise Exception("Cannot peek at an empty stack")
        return self.top.value


    def is_empty(self):

        if self.top is None:
            return True
        return False