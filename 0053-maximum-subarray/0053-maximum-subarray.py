class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        l = len(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        if l == 1:
            return nums[0]
        if l == 2:
            n = max(nums)
            return max(n, sum(nums))

        for i in range(1, len(nums)):
            
            dp[i] = max(dp[i-1]+ nums[i], nums[i])

        return max(dp)



