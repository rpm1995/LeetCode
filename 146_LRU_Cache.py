class Node:

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dicti = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dicti:
            return -1

        node = self.dicti[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dicti:
            self.remove(self.dicti[key])
            del self.dicti[key]

        node = Node(key, value)
        self.dicti[key] = node
        self.add(node)

        if len(self.dicti) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.dicti[lru.key]

    def add(self, node):
        """
        Adding a node in the doubly linked list near the tail (which is the most
        recently used side)
        """
        temp = self.tail.prev
        temp.next = node
        node.prev = temp
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        """
        Removing node from linked list
        """
        p = node.prev
        p.next = node.next
        node.next.prev = p

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
