class BinaryNode():
    def __init__(self, value, protected=False) :
        """
        Creates a new node with the given value.
        args:
            value: the value to be stored in the node.
            protected: if True, the node cannot be modified after creation outside the tree.
        """
        self._value = value
        self._left = None
        self._right = None
        self._protected = protected

    
    @property
    def value(self) : return self._value

    @value.setter
    def value(self, value) :
        if self.protected:
            raise ValueError(
                'Cannot set value on protected node, use `add` method in the tree instead.')
        self._value = value

    @property
    def left(self) : return self._left

    @left.setter
    def left(self, node) :
        if self.protected:
            raise ValueError(
                'Cannot set left node on protected node, use `add` method in the tree instead.')
        self._left = node

    @property
    def right(self) : return self._right

    @right.setter
    def right(self, node) -> None:
        if self.protected:
            raise ValueError(
                'Cannot set right node on protected node, use `add` method in the tree instead.')
        self._right = node

    @property
    def protected(self) : return self._protected