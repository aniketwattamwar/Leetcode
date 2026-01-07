import heapq
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        print(freq)
        max_heap = []
        for num, f in freq.items():
            heapq.heappush(max_heap, (-f, num))
        k_freq = []
        for i in range(k):
            f, num = heapq.heappop(max_heap)
            k_freq.append(num)

        return k_freq




