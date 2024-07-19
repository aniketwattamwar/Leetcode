class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.storage = [False for _ in range(1000001)]
         
    def hash1(self, key):
        return key%1000

    def hash2(self, key):
        return key//1000

    def add(self, key: int) -> None:
        if self.storage[key] is False:
            self.storage[key] = True

    def remove(self, key: int) -> None:
        if self.storage[key] is True:
            self.storage[key] = False
        

    def contains(self, key: int) -> bool:
        return self.storage[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)