import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap) >= 2:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            if stone1 != stone2:
                heapq.heappush(max_heap, -abs(stone1-stone2))
            
        if len(max_heap) == 1:
            return -max_heap[0]
        else:
            return 0

