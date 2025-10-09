class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        res  = []
        nums.sort()
        def rec(i, subsets):
            if i == len(nums):
                res.append(subsets.copy())
                return 
             
            subsets.append(nums[i])
            rec(i+1, subsets)
            subsets.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            rec(i+1, subsets)

        res.sort()

        rec(0,[])
        return res




        