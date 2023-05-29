
class Node():

    def __init__(self,value=None,next=None) :
        self.value = value
        self.next=next




class Queue:
    def __init__(self,front=None,back=None):
        self.front=front #first node in the queue
        self.back=back #last node in the queue

    def enqueue(self,value):
        node=Node(value)
        
        if self.back:
            self.back.next = node
        self.back = node
        if not self.front:
            self.front = node

    def dequeue(self):
        if self.front is None:
            raise Exception("Empty Queue")

        curr = self.front
        if (self.front == self.back):
            self.back = None
            self.front = None
            return curr.value

        self.front = self.front.next
        return curr.value

    def peek(self):
        if self.front is None:
            raise Exception("Empty Queue")
        
        return self.front.value
    
    def is_empty(self):
        if self.front is None:
            return True
        return False


        