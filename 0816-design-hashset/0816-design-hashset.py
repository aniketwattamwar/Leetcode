class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.storage = [[] for _ in range(1000)]
        
         
    def hash1(self, key):
        return key%1000

    def hash2(self, key):
        return key//1000

    def add(self, key: int) -> None:
        idx = self.hash1(key)
        idx2 = self.hash2(key)
        
        if self.storage[idx] == []:
            if idx == 0:
                self.storage[idx] = [False]*1001
                 
            else:
                self.storage[idx] =[False]*1000            
        self.storage[idx][idx2] = True
            
    def remove(self, key: int) -> None:
        idx = self.hash1(key)
        idx2 = self.hash2(key)
        
        if self.storage[idx] == []:
            return
        else:
            self.storage[idx][idx2] = False
        

    def contains(self, key: int) -> bool:
        idx = self.hash1(key)
        idx2 = self.hash2(key)
        
        if self.storage[idx] == []:
            return False
        return self.storage[idx][idx2]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)