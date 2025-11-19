class Node:
    def __init__(self,key, val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:
#  
    # left      (4,4)  (3,3)        right
    # least                           most
    # {1, Node(1,1)}
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    
    def _remove(self, node):
        
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def _add(self, node):
        
        self.right.prev.next = node
        node.prev = self.right.prev

        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._add(node)
            return node.val

        return -1


    def put(self, key: int, value: int) -> None:

        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self._remove(node)
            self._add(node)
            return
        
        if len(self.hashmap) == self.capacity:
            del self.hashmap[self.left.next.key]
            self._remove(self.left.next)

        node = Node(key,value)
        self.hashmap[key] = node
        self._add(node)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)