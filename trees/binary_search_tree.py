from trees.nodes.binary_node import BinaryNode
from trees.binary_tree import BinaryTree
from typing import TypeVar, Optional, Protocol, Any

# region Typing

T = TypeVar("T", bound='Comparable')


class Comparable(Protocol):
    def __eq__(self, __value) : ...
    def __ne__(self, __value): ...
    def __lt__(self, __value) : ...
    def __le__(self, __value) : ...
    def __gt__(self, __value) : ...
    def __ge__(self, __value) : ...

# endregion


class BinarySearchTree(BinaryTree):

    @property
    def root(self) :
        """Returns the root node of the tree.\n
        read-only property, Cannot set root node on binary search tree, use `add` method instead.
        """
        return self._root

    def add(self, value) :
        """Adds a value to the tree, maintaining the binary search tree property."""
        if self._root is None:
            self._root = BinaryNode(value, True)
        else:
            self._add(value, self._root)

    def _add(self, value, node) -> None:
        """recursive helper function for add method, adds a value to the tree, maintaining the binary search tree property."""
        if value <= node.value:
            if (node._left is None):
                node._left = BinaryNode(value, True)
                return
            self._add(value, node._left)
        else:
            if (node._right is None):
                node._right = BinaryNode(value, True)
                return
            self._add(value, node._right)

    def contains(self, value)  :
        """ Returns True if the value is in the tree, False otherwise."""
        return self._contains(value, self.root)

    def _contains(self, value, node) :
        """recursive helper function for contains method, returns True if the value is in the tree, False otherwise."""
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            return self._contains(value, node.left)
        else:
            return self._contains(value, node.right)