class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        ## Always an interesting prblm to solve
        ## This time I got the logic but coding and figuring out the
        ## the i - coin thing is difficult.

        dp = [0] + [amount + 1] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == amount + 1 else dp[amount]

        # if amount == 0:
        #     return 0
        # if len(coins) == 1 and coins[0] == 1:
        #     return amount
        # if len(coins) == 1 and amount %2 == 0 and coins[0]%2 != 0:
        #     return -1
        # if len(coins) == 1 and amount %2 != 0 and coins[0]%2 == 0:
        #     return -1
        # n  =len(coins)
        # dp = [0]*n
        # idx = 0
        # c = 0
        # minc = 10000
        # amt = amount
        # for i in range(n):
        #     if coins[i] > amt:
        #         break
        #     amount = amt
        #     c = 0
        #     while amount > 0:
        #         if amount < coins[i]:
        #             break
        #         amount = amount - coins[i]
        #         c+=1
        #     if amount in coins:
        #         c+=1
        #     else:
        #         while amount > 0:
        #             if amount < coins[i]:
        #                 break
        #             amount = amoutn - coins[i]
        #             c+=1
        #     minc = min(c,minc)
        

        # return min(minc,amt)
