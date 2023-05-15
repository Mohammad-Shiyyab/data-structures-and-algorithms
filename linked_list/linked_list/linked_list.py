
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        return self.to_string()

    def insert(self, value):
        old_node = self.head
        new_node = Node(value)

        new_node.next = old_node
        self.head = new_node
        self.length += 1

    def append(self,value):
        new_node=Node(value)
        if(self.head is None):
            self.head=new_node
            self.length +=1
            return
        curr=self.head

        while (curr.next is not None):
            curr=curr.next
        curr.next =new_node
        self.length +=1


    def insert_before(self,value,new_value):
        
        if self.head is None:
            self.head = Node(new_value)
        elif self.head.value == value:
            new_node = Node(new_value)
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head

            while curr.next is not None and curr.next.value != value:
                curr= curr.next

            if curr.next is None:
                curr.next = Node(new_value)
            else:
                new_node = Node(new_value)
                new_node.next = curr.next
                curr.next = new_node

    


    def insert_after(self,value,new_value):
        new_node=Node(new_value)
        curr=self.head
        while (curr is not None):
            if (curr.value==value) :
                new_node.next=curr.next
                curr.next=new_node
                return
            curr=curr.next    
        

        raise Exception ("No change, method exception") 

    def includes(self, value):
        curr = self.head
        while (curr is not None):
            if (curr.value == value):
                return True
            curr = curr.next
        return False

    def to_string(self):
        output = ""
        curr = self.head
        while (curr is not None):
            output += f"{{ {curr.value} }} -> "
            curr = curr.next
        output += "NONE"
        return output