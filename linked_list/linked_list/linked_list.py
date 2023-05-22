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
    
    def kth_from_end(self,k):

        if k < 0 :
            raise IndexError ("Enter positive index")
        
        if k > self.length:
            raise IndexError ("index out the range")

        index= self.length - k -1
        curr=self.head
        while curr is not None :
            if index ==0:
                return curr.value
            index -=1
            curr =curr.next


    def zip_lists(list1, list2):
    
        if list1.head is None:
            return list2
        if list2.head is None:
            return list1

        curr1 = list1.head
        curr2 = list2.head

        while curr1 is not None and curr2 is not None:
            next1 = curr1.next
            next2 = curr2.next
            curr1.next = curr2
            curr2.next = next1 or next
            curr1 = next1
            curr2 = next2

        return list1
        
        


