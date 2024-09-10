class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        # Exhaustive sollution to solve the problem but we get TLE
        # Go for DP

        # def helper(coins,idx,amount):

        #     # base case
        #     if amount < 0 or idx == len(coins):
        #         return 0
        #     if amount == 0:
        #         return 1
            

        #     # choose a coin
        #     case1 = helper(coins,idx,amount - coins[idx])
        #     # dont choose a coin
        #     case2 = helper(coins,idx+1,amount)
        #     return case1 + case2
        
        # return helper(coins,0,amount)

        dp = [[0 for _ in range(0,amount+1)] for _ in range(len(coins)+1)]
         

        for i in range(len(coins)+1):
            dp[i][0] = 1
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] =  dp[i-1][j] + dp[i][j-coins[i-1]]

        return dp[-1][-1]
