import heapq
from sortedcontainers import SortedDict
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        # Approach 4. The most efficient with 2 deques
        max_deque = deque()
        min_deque = deque()
        l = 0
        max_ans = 0

        for r in range(n):
            while max_deque and max_deque[-1] < nums[r]:
                max_deque.pop()
            max_deque.append(nums[r])
             

            while min_deque and min_deque[-1] > nums[r]:
                min_deque.pop()
            min_deque.append(nums[r])
            

            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[l]:
                    max_deque.popleft()
                if min_deque[0] == nums[l]:
                    min_deque.popleft()
                l+=1
            max_ans = max(max_ans, r - l +1)
                
        return max_ans
    
        
        
        # Approach 3 with sorted dicti - new concept for me
        # window = SortedDict()
        # l = 0
        # max_ans = 0
        # for r in range(n):
        #     if nums[r] in window:
        #         window[nums[r]]+=1
        #     else:
        #         window[nums[r]] = 1
         
        #     while window.peekitem(-1)[0] - window.peekitem(0)[0] > limit:
        #         window[nums[l]] -=1
        #         if window[nums[l]] == 0:
        #             window.pop(nums[l])
        #         l+=1
        #     max_ans = max(max_ans, r - l +1)
        # return max_ans
        
        
        # Approach 2 with 2 heaps
        # minheap = []
        # maxheap = []
        # l = 0
        # r = 0
        # max_ans = 0
        # ans = 0
        # for r in range(n):
        #     heapq.heappush(minheap, (nums[r], r))
        #     heapq.heappush(maxheap, (-nums[r], r))
            
        #     diff = abs(-maxheap[0][0] - minheap[0][0])
        #     if diff > limit:
        #         if minheap[0][0] == nums[l]:
        #             heapq.heappop(minheap)
        #         elif maxheap[0][0] == nums[l]:
        #             heapq.heappop(maxheap)
        #         l+=1
               
        #         ans = r - l
             

        #     max_ans = max(max_ans, ans)

        # return max_ans
            

        # TLE approach with two pointers.
        # l = 0
        # r = 0
        # min_val = 0
        # max_val = 0
        # max_ans = 0 
        # ans = 0
        # while l <= r and r < n:
            
        #     min_val = min(nums[l:r+1])
        #     max_val = max(nums[l:r+1])

        #     diff = abs(min_val - max_val)
        #     if diff > limit:
        #         l += 1
        #         ans = r - l 
        #     else:
        #         r+=1
        #         ans = r - l
        #     max_ans = max(max_ans, ans)
        
        # return max_ans
            
               


