class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l = 0
        h = len(nums)-1
        if len(nums) == 1:
            return 0
        while l<=h:

            m = l+(h-l)//2
            if (m == 0 or nums[m]>nums[m-1]) and (m == len(nums) - 1 or nums[m]> nums[m+1]):
                return m
            elif nums[m+1] > nums[m]:
                l = m+1
            else:
                h = m-1
             
        


