class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP approach
        # idx/amt -> 0   1   2   3   4   5   6   7   8   9  10  11
        # dp array   0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12
        # 1 ->       0   1  2    3   4   5   6   7   8   9  10  11
        # 2 ->       0   1  1    2   2   3   3   4   4   5  5   6
        # 5 ->       0   1  1    2   2   1   2   2   3   3  2   3

        # min(dp[i], dp[i-coin] + 1) ->   dp[1] + 1 -> 1+1 = 2

        dp = [0] + [amount+1]* amount

        for coin in coins:
            for i in range(coin,amount +1):
                dp[i] = min(dp[i],dp[i-coin] + 1)

        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]

            
