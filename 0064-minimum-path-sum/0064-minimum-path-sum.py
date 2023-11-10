class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        if rows == cols == 1:
            return grid[0][0]
        dp = [[0 for c in range(len(grid[0]))] for r in range(len(grid))]
        
        for i in range(cols):
            dp[0][i] =  grid[0][i] +dp[0][i-1]
        
        for i in range(rows):
            dp[i][0] =  grid[i][0] +dp[i-1][0]
        print(dp)
        
        for r in range(1,rows):
            for c in range(1,cols):
                dp[r][c] = grid[r][c]  + min(dp[r-1][c],dp[r][c-1])


        return dp[-1][-1]

