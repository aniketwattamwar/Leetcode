class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums = [1,2,3,1]
        # dp -> 1 
        # dp -> max(btwn two houses)
        # dp[3] = max(dp[2],nums[3]+dp[1])
        # 1,15,1
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        for i in range(2,n):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])

        return dp[-1]


