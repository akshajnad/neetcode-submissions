class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        if node == self.tail:
            return node.val

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev

        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
            return

        node = Node(key, value)
        self.cache[key] = node

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        if len(self.cache) > self.cap:
            old = self.head
            self.head = self.head.next

            if self.head:
                self.head.prev = None
            else:
                self.tail = None

            del self.cache[old.key]


class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None