class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def _insert(self,node):
        
        prev_node = self.right.prev
        nxt_node = self.right

        node.prev = prev_node
        node.next = nxt_node

        prev_node.next = node
        nxt_node.prev = node

    
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
        
    def get(self, key: int) -> int:

        if key not in self.hm:
            return -1
        
        node = self.hm[key]
        self._remove(node)
        self._insert(node)
        return node.value
        
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.hm:
            node = self.hm[key]
            node.value = value
            self._remove(node)
            self._insert(node)
            return
        
        if self.capacity <= len(self.hm):
            del self.hm[self.left.next.key]
            self._remove(self.left.next)
            
        
        node = Node(key,value)
        self._insert(node)
        self.hm[key] = node

        

            
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)