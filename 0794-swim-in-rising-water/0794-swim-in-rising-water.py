import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Understood the logic, but failed to figures out the right data structure to use

        # minHeap used with dp approach
        # saw neetcode solution, but did the code on my own after understanding

        N = len(grid)
        
        minheap = [[grid[0][0], 0, 0]]
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        seen = set()
        while minheap:
            t,r,c = heapq.heappop(minheap)

            if r == N - 1 and c == N-1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr == N or nc == N or nr < 0 or nc < 0 or (nr,nc) in seen):
                    continue
                seen.add((nr,nc))
                heapq.heappush(minheap, [max(t, grid[nr][nc]), nr, nc])
                
            
        


                

