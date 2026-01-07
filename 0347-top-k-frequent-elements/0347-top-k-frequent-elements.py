import heapq
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        freq = Counter(nums)
        min_heap = []

        for num, f in freq.items():
            heapq.heappush(min_heap, (f,num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            

        print(min_heap)
        ans = []
        for i in range(len(min_heap)):
            f,n = heapq.heappop(min_heap)
            ans.append(n)
        return ans

        # Got below soution on my own, but the max heap is a trap and the solution is NlogN
        # freq = Counter(nums)
        # print(freq)
        # max_heap = []
        # for num, f in freq.items():
        #     heapq.heappush(max_heap, (-f, num))
        # k_freq = []
        # for i in range(k):
        #     f, num = heapq.heappop(max_heap)
        #     k_freq.append(num)

        # return k_freq




