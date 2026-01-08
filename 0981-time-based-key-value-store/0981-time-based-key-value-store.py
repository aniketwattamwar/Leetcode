import collections
import bisect
class TimeMap:

    def __init__(self):
        self.map  = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
        else:
            self.map[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:

        if key in self.map:
            values = self.map[key]
             
            idx = bisect.bisect_right(values, (timestamp, chr(127)))
            if idx == 0:
                return "" 
            return values[idx - 1][1]
        
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)