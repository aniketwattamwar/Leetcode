nums = [-2,1,-3,4,-1,2,-5,4]

def maxSubArray(nums):
        
        max_val = nums[0]
        currSum = 0
        
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum+=num
            max_val = max(currSum, max_val)
        return max_val

m = maxSubArray(nums)
print(m)