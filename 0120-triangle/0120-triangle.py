class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:


        l = len(triangle)

        for i in range(l-2,-1,-1):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]

        ## Used DP solves for all positive numbers. Fails when negative numbers appear since 
        ## addition with negative numbers can yeild smaller path

        # if len(triangle) == 1:
        #     return triangle[0][0]
        # rows = len(triangle)
        # cols  = len(triangle[-1])
        # dp = [[10000 for c in range(cols)] for r in range(rows)]
         
        # dp[1][0] = triangle[0][0] + triangle[1][0]
        # dp[1][1] = triangle[0][0] + triangle[1][1]

        
        # for r in range(2,rows):
        #     for c in range(cols):
        #         mini  = min(dp[r-1])
        #         if c < len(triangle[r]):
        #             dp[r][c] = mini +  triangle[r][c]
        
       
                 


        # return min(dp[-1])



        