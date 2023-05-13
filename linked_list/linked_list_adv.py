from typing import TypeVar, Generic, Union

T = TypeVar("T")


class Node(Generic[T]):

    def __init__(self, value) :
        self.value = value
        self.next: Union[Node, None] = None


class LinkedList(Generic[T]):

    def __init__(self) :
        self.head:  Union[Node, None] = None
        self.length = 0

    def __str__(self):
        return self.to_string()

    def __iter__(self):
        curr = self.head
        while (curr is not None):
            yield curr
            curr = curr.next

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Index must be positive")

        for i, node in enumerate(self):
            if i == index:
                return node
        raise IndexError("Index out of range")

    def __len__(self):
        return self.length

    def insert(self, value):
        old_node = self.head
        new_node = Node(value)

        new_node.next = old_node
        self.head = new_node
        self.length += 1

    def includes(self, value: T) :
        for node in self:
            if node.value == value:
                return True
        return False

    def to_string(self):
        output = ""
        for node in self:
            output += f"{{ {node.value} }}  "
        output += "NONE"
        return output

    def insert_multiple(self, values):
        for value in values:
            self.insert(value)

    def append(self, value: T):
        new_node = Node(value)
        if (self.head is None):
            self.head = new_node
            self.length += 1
            return

        curr = self.head
        while (curr.next is not None):
            curr = curr.next
        curr.next = new_node
        self.length += 1

    def delete(self, value: T):
        curr = self.head
        prev = None

        while (curr is not None):
            if (curr.value == value):
                if (prev is None):
                    self.head = curr.next
                else:
                    prev.next = curr.next
                self.length -= 1
                return
            prev = curr
            curr = curr.next