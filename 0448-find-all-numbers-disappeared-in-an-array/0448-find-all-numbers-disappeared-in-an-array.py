class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        final_nums = []
        ans = [False]*len(nums)
        for i in range(len(nums)):
            ans[nums[i]-1] = True

        for i,v in enumerate(ans):
            if  v == False:
                final_nums.append(i+1)

        return final_nums

