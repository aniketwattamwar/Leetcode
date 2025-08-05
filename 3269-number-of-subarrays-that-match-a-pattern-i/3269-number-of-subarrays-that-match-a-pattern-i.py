class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
    #    understoo the logic and partial code on my own
    #   but struggled with the innnerloop abit

        
        count = 0  
        m = len(pattern)
        n  = len(nums)
        for i in range(n-m):
            check = True
            for j in range(len(pattern)):
                a, b = nums[i+j], nums[i+j+1]
                if pattern[j] == 1 and not (b > a):
                    check = False
                    break
                if pattern[j] == 0 and not (b==a):
                    check=False
                    break
                if pattern[j] == -1 and not (a>b):
                    check = False
                    break
                
            if check:
                count+=1

        return count







        