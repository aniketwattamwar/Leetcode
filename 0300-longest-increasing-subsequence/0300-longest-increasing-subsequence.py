class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # The below code solves 17/54 test cases using partial brute force.
        # m = len(nums)
        # m  = 0
        # ans = []
        # for i in range(len(nums)):
        #     ans.append(nums[i])
        #     for j in range(i,len(nums)):
        #         if nums[i] < nums[j]:
        #             ans.append(nums[j])
        #             print(ans)
        #             i = j
        #     if len(ans)> m:
        #         m = len(ans)
        #     ans = []
        # return m

        dp = [1 for _ in range(len(nums))]
        ans = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    ans = max(dp[i],ans)
        return ans



















