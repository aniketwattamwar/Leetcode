class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # # DP Table
        #   0  1  2  3  4  5
        # 0 1  0  0  0  0  0
        # 1 1  1  1  1  1  1
        # 2 1  1  2  2  3  3
        # 5 1  1  2  2  3  4
        #  choose or dont choose
        
        dp = [[0 for _ in range(0,amount+1)] for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                        # not choose + choose
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]


        return dp[-1][-1]

        
