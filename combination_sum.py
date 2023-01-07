def combinationSum(candidates, target):
    nums = sorted(candidates)
    res = []
    backtracking([],0,nums,target)
    return res
def backtracking(subset,start,nums,target):
    #print(.res,subset)
    if target == 0:
        res.append(list(subset))
    for i in range(start,len(nums)):
        if nums[i] > target: 
            break
        subset.append(nums[i])
        backtracking(subset,i,nums,target-nums[i])
        subset.pop()