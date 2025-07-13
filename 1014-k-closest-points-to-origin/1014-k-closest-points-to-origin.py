import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Below code works for 84/87 cases
        # the problem with mapping is same distance for different points is possible
        # so it overwrites
        # You dont need the mappping add the point in the min_heap itself.
###########################
        # min_heap = []
        # mapping = {}
        # ans =[]
        # heapq.heapify(min_heap)
        # def calc_dist(x,y):
        #     d = math.sqrt(pow(x-0,2)+pow(y-0,2))
        #     return d

        # for point in points:
        #     x,y = point[0],point[1]
        #     d = calc_dist(x,y)
        #     mapping[d] = point
        #     heapq.heappush(min_heap,d)

        # for _ in range(k):
        #     d = heapq.heappop(min_heap)
        #     ans.append(mapping[d])

        # return ans

        min_heap = []
        ans =[]
        heapq.heapify(min_heap)
        def calc_dist(x,y):
            d = math.sqrt(pow(x-0,2)+pow(y-0,2))
            return d

        for point in points:
            x,y = point[0],point[1]
            d = calc_dist(x,y)
            
            heapq.heappush(min_heap,(d,point))

        for _ in range(k):
            d,point = heapq.heappop(min_heap)
            ans.append(point)

        return ans


