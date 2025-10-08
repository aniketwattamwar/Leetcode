class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res = []

        def rec(permutation):
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return

            for i in range(0, len(nums)):
                if nums[i] not in permutation:
                    permutation.append(nums[i])
                    rec(permutation)
                    permutation.pop()

        
        rec([])
        return res

