import heapq
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
             
        # d = Counter(nums)


        # sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        # print(sorted_d)
        # ans = []
        # for i in range(k):
        #     k,f = sorted_d[i]
        #     print(sorted_d[i])
        #     ans.append(k)
        # return ans

        import heapq
        d = Counter(nums)
        h = []
        for key,f in d.items():
            if len(h) >= k:
                if f > h[0][0]:
                    heapq.heappop(h)
                    heapq.heappush(h, (f,key))
            else:
                heapq.heappush(h,(f,key))

        topk=[]
        print(h)
        for ele in h:
            topk.append(ele[1])

        print(topk)
        return topk


