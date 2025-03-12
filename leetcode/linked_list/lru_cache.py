class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node
        # dummy nodes
        # left = LRU, right = MRU
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        # connect the dummy nodes, when we insert a node it will go between these two dummy nodes
        self.left.next = self.right
        self.right.prev = self.left

    # helper method to remove node from linked list
    # we will always remove a node in between two other nodes thanks to the dummy nodes
    def remove(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.next = nxt
        nxt.prev = prev
        # the node is now no longer in between prev and nxt

    # helper method to insert node at right most position of linked list
    # insert right before our right pointer (the right dummy node)
    def insert(self, node):
        # getting nodes that we will be inserting inbetween
        prev = self.right.prev
        nxt = self.right
        # updating nodes to point to new node
        prev.next = node
        nxt.prev = node
        # adding next and prev pointers for new node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # update the node to the most recently used node
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val  # .val because the value for the cache is a pointer to node
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from list and delete/evict the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
