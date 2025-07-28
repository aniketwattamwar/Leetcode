class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        # res = [[]]
        
        # for num in nums:
        #     res += [subset + [num] for subset in res]
        
        # return res

        result  = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return result