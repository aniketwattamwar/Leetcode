class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      
        max_area = 0

        def rec(i,j):
            
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 2
            return 1 + rec(i+1,j) + rec(i,j+1) + rec(i-1,j) + rec(i,j-1)


        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = rec(i,j) 
                    max_area = max(max_area, area)

        return max_area












