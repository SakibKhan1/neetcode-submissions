# Define a doubly-linked list node
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val  # store both key and value for eviction
        self.prev = self.next = None  # initialize pointers to previous and next nodes

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity           # max number of items LRU cache can hold
        self.cache = {}              # hashmap: key -> Node for O(1) access

        # dummy head (left) and tail (right) nodes to simplify edge operations
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left  # connect head and tail

    # Removes a node from the doubly linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next       # grab surrounding nodes
        prev.next, nxt.prev = nxt, prev        # link them to each other, skipping node

    # Inserts a node right before the right (tail) — most recently used position
    def insert(self, node):
        prev, nxt = self.right.prev, self.right  # get last real node and dummy tail
        prev.next = nxt.prev = node              # attach new node between them
        node.next, node.prev = nxt, prev         # point node to its neighbors

    # Get the value associated with a key
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])        # move node to the end (MRU)
            self.insert(self.cache[key])
            return self.cache[key].val          # return stored value
        return -1                               # key doesn't exist

    # Insert or update the value for a key
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])        # remove old node if exists

        self.cache[key] = Node(key, value)      # create new node and update hashmap
        self.insert(self.cache[key])            # insert as most recently used

        if len(self.cache) > self.cap:          # check if over capacity
            lru = self.left.next                # least recently used node is next to dummy head
            self.remove(lru)                    # remove it from linked list
            del self.cache[lru.key]             # also remove from hashmap
