from collections import defaultdict
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        
        # defaultdict(<class 'list'>, { 0: [(1, 10)], 
        #                               1: [(0, 10), (2, 11), (3, 13)], 
        #                               2: [(1, 11), (3, 12)], 
        #                               3: [(2, 12), (1, 13)]})

        visited = [0] * len(values)
        graph = defaultdict(list)
        for u,v, time in edges:
            graph[u].append((v,time))
            graph[v].append((u,time))

        max_quality = 0
        def dfs(node, time, val):
            nonlocal max_quality
            if node == 0:
                max_quality = max(max_quality, val)
            for neighbor, curr_time in graph[node]:

                if curr_time + time <= maxTime:
                    new_val = 0 
                    if visited[neighbor] == 0:
                        new_val += values[neighbor]
                    else:
                        new_val+=0
                    visited[neighbor]+=1
                    dfs(neighbor, curr_time+time, val + new_val)
                    visited[neighbor]-=1
        
        visited[0] = 1
        dfs(0,0,values[0])
        return max_quality





