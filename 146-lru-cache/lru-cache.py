class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.map = {}
        self.length = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            tmp = self.map[key]
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev

            tmp.prev = self.tail.prev
            self.tail.prev.next = tmp
            tmp.next = self.tail
            self.tail.prev = tmp

            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            tmp = self.map[key]
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev

            tmp.prev = self.tail.prev
            self.tail.prev.next = tmp
            tmp.next = self.tail
            self.tail.prev = tmp

            tmp.val = value
            return

        newNode = Node(key, value)
        self.map[key] = newNode

        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev.next = newNode
        self.tail.prev = newNode

        self.length += 1

        if self.length > self.capacity:
            tmp = self.head.next
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            del self.map[tmp.key]
            self.length -= 1
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)