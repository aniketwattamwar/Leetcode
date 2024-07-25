# Basically the idea is to create an array and at each idx in that array is the start of a linked list.
# when key is given, you hash it and at that location you store the value
# but since collisions can occur we maintain a LL at the indexes.

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000001
        self.arr = [None]* self.size


# To put the value at a particular key, hash value is calculated

    def put(self, key: int, value: int) -> None:
        idx = key% self.size
        if self.arr[key] == None: # check if at the value is there collision, 
            self.arr[idx] = ListNode(key,value) #if not simply create a node and add the value to that key
            return
        curr = self.arr[idx] # but collision occurs
        while curr:          # iterate the LL till end
            if curr.key == key:   # case when we are update a value at a key
                curr.val = value
                return
            if not curr.next:    #new key  and new value so Node created by iterating
                curr.next = ListNode(key,value)
                return
            curr = curr.next

    def get(self, key: int) -> int:
        idx = key % self.size   # populated the hash idx
        curr = self.arr[idx]    # we see there is a LL head here
        while curr:             # we iterate
            if curr.key == key: # we find the key, the user is looking for
                return curr.val # we return the val
            curr = curr.next 
        return -1               # no key, value found reutrn -1
        

    def remove(self, key: int) -> None:
        idx = key % self.size    # populated the hash idx
        curr = self.arr[idx]     # we see there is a LL head here

        if not curr:
            return
        if curr.key == key:      # we check if the first node is what we want to remove 
            self.arr[idx] = curr.next   # if yes simply assign the arr frst node to next
            return

        while curr.next:        # first node is not the one we want to remove, we iterate then
            if curr.next.key == key:        # found what we want to remove
                curr.next = curr.next.next  # skkip the next to next.next and remove it
                return
            curr = curr.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)