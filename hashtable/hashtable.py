
from typing import Generic, TypeVar, Optional

K = TypeVar('K')
V = TypeVar('V')


class Hashtable(Generic[K, V]):
    def __init__(self, size = 100) :
        self._size: int = size
        self._buckets: list[Optional[list[tuple[K, V]]]] = [None] * size

    @property
    def size(self) :
        """
        Get the size of the hashtable
        """
        return self._size

    def set(self, key, value) :
        """
        Insert a new key-value pair into the hashtable
        """
        hash = self._hash(key)

        if (bucket := self._buckets[hash]) is None:
            bucket = []

        bucket.append((key, value))
        self._buckets[hash] = bucket

    def get(self, key) :
        """ 
        Get the value associated with a key
        """
        hash = self._hash(key)

        if (bucket := self._buckets[hash]) is None:
            return None

        for k, v in bucket:
            if k == key:
                return v

        return None

    def has(self, key) :
        """
        Check if a key exists in the hashtable
        """
        hash = self._hash(key)

        if (bucket := self._buckets[hash]) is None:
            return False

        for k, _ in bucket:
            if k == key:
                return True

        return False

    def keys(self) :
        """
        Get all the keys in the hashtable
        """
        keys = []
        for bucket in self._buckets:
            if bucket is not None:
                for k, _ in bucket:
                    keys.append(k)

        return keys

    def _hash(self, key) :
        """
        Hash a key
        """
        # from ascii to unicode
        hash: int = 0

        for char in str(key):
            hash += ord(char)

        return hash % self.size