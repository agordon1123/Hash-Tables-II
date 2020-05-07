class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    """
    Holds the head
    """
    def __init__(self, head):
        self.head = head

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037
        hash = offset_basis
        for i in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(i)
        return hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        pass

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:
            self.storage[index] = LinkedList(HashTableEntry(key, value))
        else:
            ll = self.storage[index]
            node = ll.head
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev = node
                node = node.next
            prev.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is not None:
            ll = self.storage[index]
            node = ll.head
            prev = None
            while node:
                if node.key == key:
                    if prev is not None:
                        prev.next = node.next
                        return node.value
                    temp = node
                    ll.head = node.next
                    return temp.value
                node = node.next
        else:
            print("Warning - Key not found")
            return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is not None:
            ll = self.storage[index]
            node = ll.head
            while node:
                if node.key == key:
                    return node.value
                node = node.next
            return None
        else:
            return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        prev_storage = list(self.storage)
        self.capacity *= 2
        self.storage = [None] * self.capacity
        for i in prev_storage:
            if i is not None:
                ll = i
                node = ll.head
                while node:
                    self.put(node.key, node.value)
                    node = node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
