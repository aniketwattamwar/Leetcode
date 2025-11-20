import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # nums = [3,2,1,5,6,4], k = 2
        # sorted = [1,2,3,4,5,6]  return n-k+1
        # [ 5, 6 ]

        min_heap = nums
        heapq.heapify(min_heap)
        while len(min_heap) > k:
            heapq.heappop(min_heap)

        return min_heap[0]



