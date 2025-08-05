from collections import defaultdict
class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        # this was not medium problem quite hard even to understand
        # used chatgpt to figure it out
        mapping = defaultdict(int)

        for i,j in coordinates: 
            
            for dx in [0,-1]:
                for dy in [0,-1]:
                    x = i+dx
                    y = j+dy
                    if 0<= x < m - 1 and 0 <= y < n-1:
                        mapping[(x,y)]+=1

        arr = [0]*5
        # print(mapping)
        for count in mapping.values():
            arr[count]+=1
        # print(arr)
        total = (m-1)*(n-1)
        arr[0] = total - sum(arr[1:])
        return arr
