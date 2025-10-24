class TimeMap:

    def __init__(self):
        self.keytimeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.keytimeMap:
            self.keytimeMap[key] = []
        self.keytimeMap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        
        if not key in self.keytimeMap:
            return ""
        
        all_values = self.keytimeMap[key]
         
        left = 0 
        right = len(self.keytimeMap[key])
        while left < right:

            mid = (left + right)//2
            if self.keytimeMap[key][mid][0] <= timestamp:
                left  = mid+1
            else:
                right = mid 

        return "" if right == 0 else self.keytimeMap[key][right - 1][1]





# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)